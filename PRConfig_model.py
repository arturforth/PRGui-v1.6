import ctypes
import os
import shutil
from PRConfig_ui import *
from lxml import etree


# Clase que representa al Modelo dentro del esquema Model-View-Controller.
# class Model(QtWidgets.QMainWindow, Ui_MainWindow):
class Model(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, filename, carpeta):
        super().__init__()

        self.filename = filename
        self.modificado = False        # Permite llevar un registro de la realizacion de cambios en los archivos.

        # self.crearBackup(carpeta)      # Se crea un backup del archivo de config. en la carpeta 'carpeta'

        if self.filename[0:3] == 'BAP':
            self.rootname = 'BAPList'
            self.dispositivo = 'BAP'
        elif self.filename[0:3] == 'Con':
            self.rootname = 'ConsoleList'
            self.dispositivo = 'Console'
        elif self.filename[0:3] == 'Kan':
            self.rootname = 'KantList'
            self.dispositivo = 'Kant'

        try:
            self.parser = etree.XMLParser(remove_blank_text=True)
            self.tree = etree.parse(self.filename, parser=self.parser)
            self.root = self.tree.getroot()
        except etree.ParseError:    # Archivo .dat vacio
            if self.filename == 'Spools_PRManager.config':  # En el caso de spools_PRManager no se crea un archivo.
                exit()

            self.root = etree.Element(self.rootname)
            self.tree = etree.ElementTree(self.root)
        except OSError:     # No existe el archivo .dat y lo crea.
            ctypes.windll.user32.MessageBoxW(0, 'Archivo {0} no encontrado'.format(self.filename), 'Error', 0)

            self.root = etree.Element(self.rootname)
            # Si no existe el archivo .config sale del programa
            if self.filename == 'Spools_PRManager.config':
                exit()

            if self.filename == 'BAPInfoManager.dat':
                configuration = etree.SubElement(self.root, 'Configuration')
                etree.SubElement(configuration, 'BAP3')
                etree.SubElement(configuration, 'Tabs')
                etree.SubElement(configuration, 'Botones')

            self.tree = etree.ElementTree(self.root)
            self.tree.write(self.filename, pretty_print=True, xml_declaration=True, encoding='utf-8')

    # Se ejecuta cuando se termina de crear la ventana y levanta los datos de los archivos .dat
    # En el caso de BAPInfoManager.dat solo carga las placas BAP2
    def loadDat(self, lista, configgroupbox, removerbutton, tipoBAP='BAP2', args=None):
        lista.clear()

        for i in range(len(self.root)):
            if self.root[i].tag not in ['BAP', 'Kant', 'Console']:
                continue

            # Excluye de la carga las placas que no son 'tipoBAP'
            if self.root[i].tag == 'BAP':
                if self.root[i].attrib['TipoPlaca'] != tipoBAP:
                    continue

            cant = lista.count()
            item = QtWidgets.QListWidgetItem()
            item.setText(self.dispositivo + ' {0}'.format(cant + 1))
            lista.addItem(item)

        # Tab 4 BAP3
        if removerbutton is None and configgroupbox is None:
            self.__setDisabled(lista, None, None, None, args)
        # Tab 2, Tab 3, Tab 5 y Tab 7
        else:
            if lista.count() == 0:
                removerbutton.setDisabled(True)
                configgroupbox.setDisabled(True)

        # # Si no hay ninguna placa cargada se deshabilita el boton "remover BAP/Consola/Kant" y el panel de configuracion
        # if removerbutton is not None and configgroupbox is not None:    # para tab 2, tab 3, tab 5 y tab 7
        #     if lista.count() == 0:
        #         removerbutton.setDisabled(True)
        #         configgroupbox.setDisabled(True)

        # else:   # para tab 4
        #     if lista.count() == 0:
        #         estado = True
        #
        #         # Cuando no hay BAP3 cargadas no puede haber Botones ni Eventos
        #         args.listaEventosTab4.clear()
        #         args.listaBotonesTab4.clear()
        #
        #         lista.setDisabled(estado)
        #         args.listaEventosTab4.setDisabled(estado)
        #         args.listaBotonesTab4.setDisabled(estado)
        #         args.removerBotonTab4.setDisabled(estado)
        #         args.agregarBotonTab4.setDisabled(estado)
        #         args.removerEventoTab4.setDisabled(estado)
        #         args.agregarEventoTab4.setDisabled(estado)
        #
        #         args.labelAccionTab4.setVisible(not estado)
        #         args.labelSalidaTab4.setVisible(not estado)
        #         args.labelTiempoTab4.setVisible(not estado)
        #         args.labelRtaOKTab4.setVisible(not estado)
        #
        #         args.comboBox1Tab4.setVisible(not estado)
        #         args.spinBox1Tab4.setVisible(not estado)
        #         args.spinBox2Tab4.setVisible(not estado)
        #         args.comboBox2Tab4.setVisible(not estado)

        # Por defecto el primer elemento se selecciona el primer elemento de la lista (si es que hay)
        lista.setCurrentRow(0)

    # Carga tabs y botones del tab 1 cuando inicia el programa
    def loadDatConfig(self, listaTabs, listaBotones, listaEventos, args, itemEdit=True):
        # Borra todos los elementos de las listas previamente
        listaTabs.clear()
        listaBotones.clear()
        listaEventos.clear()

        for i in range(len(self.root)):
            if self.root[i].tag == 'Configuration':
                for j in range(len(self.root[i])):
                    if self.root[i][j].tag == 'BAP3':
                        try:
                            outsnum = self.root[i][j].attrib['OutsNum']
                        except KeyError:
                            self.root[i][j].attrib['OutsNum'] = '0'
                            outsnum = '0'

                        args.spinBoxOutsNumTab1.setValue(int(outsnum))

                    if self.root[i][j].tag == 'Tabs':
                        for k in range(len(self.root[i][j])):
                            if self.root[i][j][k].tag == 'Tab':
                                item = QtWidgets.QListWidgetItem()
                                item.setText(self.root[i][j][k].attrib['id'])
                                item.setFlags(int(item.flags()) | QtCore.Qt.ItemIsEditable)
                                listaTabs.addItem(item)
                    if self.root[i][j].tag == 'Botones':
                        if len(self.root[i][j]) != 0:   # El tag Botones contiene elementos.
                            for m in range(len(self.root[i][j])):
                                if self.root[i][j][m].tag == 'Boton':
                                    cant = listaBotones.count()
                                    item = QtWidgets.QListWidgetItem()
                                    try:
                                        nombre = 'Boton {0}: {1}'.format(cant + 1, self.root[i][j][m].attrib['id'])
                                    except KeyError:
                                        nombre = 'Boton {0}'.format(cant + 1)

                                    item.setText(nombre)
                                    if itemEdit is True:
                                        item.setFlags(int(item.flags()) | QtCore.Qt.ItemIsEditable)
                                    listaBotones.addItem(item)

                                    # Genera el tooltip a partir del nombre de archivo de la imagen utilizada como icono
                                    for n in range(len(self.root[i][j][m])):
                                        if self.root[i][j][m][n].tag == 'Icon':
                                            for o in range(len(self.root[i][j][m][n])):
                                                if self.root[i][j][m][n][o].tag == 'Boton':
                                                    nombreImagenBoton = self.root[i][j][m][n][o].text
                                                    tooltip = self.__getNombreImagenBoton(nombreImagenBoton)
                                                    item.setToolTip(tooltip)    # Esto llama a itemChanged
                                                    break

        self.__setDisabledConfig(listaBotones, listaEventos, args)

        listaBotones.setCurrentRow(0)

    # Se ejecuta cuando se termina de crear la ventana y levanta los datos de los archivos .config
    def loadConfig(self, args):
        # print('loadConfig')
        dirconsola = self.readTag(self.root, 'PROperListener', 'LogFile', atributo='ConsoleAddress')
        tcpserverlistener = self.readTag(self.root, 'PROperListener', 'TCPServerListener', atributo='Address')
        udpserverlistener = self.readTag(self.root, 'PRBAPListener', 'UDPServerListener', atributo='Address')
        nronodo = self.readTag(self.root, 'KantCommModule', 'PRManager', atributo='NroNodoLocal')
        udpserveraddress = self.readTag(self.root, 'KantCommModule', 'UDPServerListener', atributo='Address')

        sendstatus = self.readTag(self.root, 'BAPKeepAlive', 'BAPAliveConfig', 'SendStatusIO')
        secstoprev = self.readTag(self.root, 'BAPKeepAlive', 'BAPAliveConfig', 'SecondsToPrevention')
        numalives = self.readTag(self.root, 'BAPKeepAlive', 'BAPAliveConfig', 'NumAlivesToNormalize')

        sendstatus = sendstatus.capitalize()

        chkinterv = self.readTag(self.root, 'BAPKeepAlive', 'CheckInterval', atributo='value')
        defaultttime = self.readTag(self.root, 'BAPKeepAlive', 'BAPConfig', 'DefaultTestTime')
        autouppar = self.readTag(self.root, 'BAPKeepAlive', 'BAPConfig', 'AutoUpdateParams')

        autouppar = autouppar.capitalize()

        args.lineEdit1Consola.setText(dirconsola)
        args.lineEdit2Consola.setText(tcpserverlistener)
        args.lineEdit3Consola.setText(udpserverlistener)
        args.lineEditNodoKant.setText(nronodo)
        args.lineEditUDPKant.setText(udpserveraddress)

        args.comboBoxStatusBAPAlive.setCurrentText(sendstatus)
        args.comboBoxAutoBAPAlive.setCurrentText(autouppar)

        args.spinBoxSegsBAPAlive.setValue(int(secstoprev))
        args.spinBoxNumBAPAlive.setValue(int(numalives))

        args.spinBoxCheckBAPConfig.setValue(int(chkinterv))
        args.spinBoxDefaultBAPConfig.setValue(int(defaultttime))

    # Para escribir en Spools_PRManager.config (tab 7) los datos ingresados desde la GUI.
    def writeConfig(self, args, linea, name=None, etiqueta1=None, etiqueta2=None, atributo=None):
        # print('writeConfig')
        self.modificado = True   # Cada vez que se hace un cambio se actualiza este flag

        names = ['PROperListener', 'PRBAPListener', 'BAPKeepAlive', 'KantCommModule']

        try:
            texto = linea.text()    # Texto que ingresa el usuario.
        except AttributeError:
            texto = linea.currentText()
            texto = texto.casefold()

        checkinterval = args.spinBoxCheckBAPConfig.text()
        secondstoprevention = args.spinBoxSegsBAPAlive.text()

        if etiqueta1 == 'LogFile':  # En este caso se tienen que modificar todos los tags con el mismo parametro.
            for name in names:
                self.writeTag(self.root, name, etiqueta1, etiqueta2, atributo, texto)
        elif name == 'PRBAPListener' and etiqueta1 == 'UDPServerListener':  # Se tienen que modificar dos tags.
            self.writeTag(self.root, name, etiqueta1, etiqueta2, atributo, texto)
            self.writeTag(self.root, 'BAPKeepAlive', 'BAPConfig', 'PRManagerAddress', val=texto)
        else:
            if etiqueta2 == 'SecondsToPrevention':
                if texto.isdigit() and checkinterval.isdigit():
                    if int(texto) >= int(checkinterval):    # SecondsToPrevention tiene que ser >= que CheckInterval
                        self.writeTag(self.root, name, etiqueta1, etiqueta2, atributo, texto)
                    else:
                        args.spinBox1BAPConfig.setValue(int(secondstoprevention))
            elif etiqueta1 == 'CheckInterval':
                if texto.isdigit() and checkinterval.isdigit():
                    if int(texto) <= int(secondstoprevention):  # CheckInterval tiene que ser <= que SecondsToPrevention
                        self.writeTag(self.root, name, etiqueta1, etiqueta2, atributo, texto)
                    else:
                        args.spinBox1BAPConfig.setValue(int(secondstoprevention))
            else:
                self.writeTag(self.root, name, etiqueta1, etiqueta2, atributo, texto)

    # Para escribir en los archivos InfoManager.dat los datos ingresados desde la GUI.
    def writeDat(self, lista, linea, numlinea, tipoBAP='BAP2'): # TODO: ver que otro nombre mejor se le puede poner
        # print('writeDat')
        self.modificado = True   # Cada vez que se hace un cambio se actualiza este flag

        seldispositivo = lista.currentRow()

        posdispositivo = self.__findPosBAP(seldispositivo, tipoBAP)

        if numlinea is 1:
            if self.dispositivo is 'Kant':
                self.root[posdispositivo].attrib['nronodo'] = linea.text()
            else:
                self.root[posdispositivo].attrib['id'] = linea.text()
        else:
            self.root[posdispositivo][numlinea-2].text = linea.text()

    # Lee el tag correspondiente y devuelve el valor del mismo. En caso de no encontrar el tag, devuelve -1
    def readTag(self, root, name, etiqueta1, etiqueta2=None, atributo=None):
        # print('readTag')
        for i in range(len(root)):
            try:
                if name == (root[i].attrib['Name']):
                    for j in range(len(root[i])):
                        for k in range(len(root[i][j])):
                            if root[i][j][k].tag == etiqueta1:
                                if etiqueta2 is None:   # No hay etiqueta2 => los tags tienen atributos
                                    return root[i][j][k].attrib[atributo]
                                for m in range(len(root[i][j][k])):
                                    if root[i][j][k][m].tag == etiqueta2:   # Si hay etiqueta2 => los tags tienen texto
                                        return root[i][j][k][m].text
                                return -1     # etiqueta2 no coincide con ningun tag del archivo
            except KeyError:    # El tag no posee atributo 'Name'
                continue

    # Escribe val en el tag indicado en los parametros. Devuelve -1 si no encuentra el tag.
    def writeTag(self, root, name, etiqueta1, etiqueta2=None, atributo=None, val=None):
        # print('writeTag')
        for i in range(len(root)):
            try:
                if name == (root[i].attrib['Name']):
                    for j in range(len(root[i])):
                        for k in range(len(root[i][j])):
                            if root[i][j][k].tag == etiqueta1:
                                if etiqueta2 is None:   # No hay etiqueta2 => los tags tienen atributos
                                    root[i][j][k].attrib[atributo] = val
                                    return None
                                for m in range(len(root[i][j][k])):
                                    if root[i][j][k][m].tag == etiqueta2:   # Si hay etiqueta2 => los tags tienen texto
                                        root[i][j][k][m].text = val
                                        return None
                                return -1     # etiqueta2 no coincide con ningun tag del archivo
            except KeyError:    # El tag no posee atributo 'Name'
                continue

    # Boton "agregar". Agrega el dispositivo correspondiente al final de cada lista.
    def agregarDisp(self, lista, configgroupbox, labels, tipoPlaca='BAP2', args=None):
        self.modificado = True   # Cada vez que se hace un cambio se actualiza este flag

        cant = lista.count()

        if cant == 0:   # No hay ningun dispositivo cargado en el archivo.
            nombre = self.dispositivo + ' {0}'.format((cant+1))
        else:
            nombre = (lista.item(cant-1)).text()
            numero = int(nombre[len(self.dispositivo):])
            numero = str(numero + 1)
            nombre = nombre[0:len(self.dispositivo)] + ' ' + numero

        item = QtWidgets.QListWidgetItem()
        item.setText(nombre)
        lista.addItem(item)

        if self.dispositivo == 'Kant':
            attrib = {'nronodo': '', 'enabled': 'true'}  # En KantsInfoManager.dat id es nronodo.
        elif self.dispositivo == 'BAP':
            attrib = {'id': '', 'enabled': 'true', 'TipoPlaca': tipoPlaca}
        else:
            attrib = {'id': '', 'enabled': 'true'}

        tmp = etree.SubElement(self.root, self.dispositivo, attrib=attrib)

        for label in labels:
            etree.SubElement(tmp, label)

        lista.setCurrentRow(cant)
        configgroupbox.setDisabled(False)

        # # Caso BAP3
        # if args is not None:
        #     estado = False
        #
        #     args.listaBAP3Tab4.setDisabled(estado)
        #     args.listaBotonesTab4.setDisabled(estado)
        #     args.agregarBotonTab4.setDisabled(estado)

    # Agregar Botones tab 1
    def agregarBotonConfig(self, listaBotones, listaEventos, args):
        rutaImagenBoton, tipos = QFileDialog.getOpenFileName(self, 'Abrir imagen', 'resources/', 'Image Files (*.png *.jpg *.bmp)')  # Ruta del archivo imagen

        if not rutaImagenBoton:
            return

        nombreImagenBoton = self.__getNombreImagenBoton(rutaImagenBoton)  # Obtiene el nombre del archivo imagen

        for i in range(len(self.root)):
            if self.root[i].tag == 'Configuration':
                for j in range(len(self.root[i])):
                    if self.root[i][j].tag == 'Botones':
                        boton = self.__botonGen(self.root[i][j], nombreImagenBoton)
                        self.root[i][j].append(boton)

                        cant = listaBotones.count()

                        if cant == 0:  # No hay ningun dispositivo en la lista.
                            nombre = 'Boton {0}:'.format((cant + 1))
                        else:
                            nombre = (listaBotones.item(cant - 1)).text()
                            numero = int(nombre[len('Boton'):nombre.find(':')])
                            numero = str(numero + 1)
                            nombre = nombre[0:len('Boton')] + ' ' + numero + ':'

                        item = QtWidgets.QListWidgetItem()
                        item.setText(nombre)
                        item.setToolTip(nombreImagenBoton)
                        item.setFlags(int(item.flags()) | QtCore.Qt.ItemIsEditable)
                        listaBotones.addItem(item)
                        listaBotones.setCurrentRow(cant)
                        self.modificado = True  # Cada vez que se hace un cambio se actualiza este flag
                        break

        self.__setDisabledConfig(listaBotones, listaEventos, args)

    # Agregar Evento en el tag Configuration tab 1
    def agregarEventoConfig(self, listaBotones, listaEventos, args):
        selBoton = listaBotones.currentRow()
        # cant = listaEventos.count()

        if selBoton == -1:
            return

        for i in range(len(self.root)):
            if self.root[i].tag == 'Configuration':
                for j in range(len(self.root[i])):
                    if self.root[i][j].tag == 'Botones':
                        for k in range(len(self.root[i][j][selBoton])):
                            if self.root[i][j][selBoton][k].tag == 'Eventos':
                                # Agrega el evento al archivo .dat
                                evento = self.__eventoGen(self.root[i][j][selBoton][k])
                                self.root[i][j][selBoton][k].append(evento)

                                cant = listaEventos.count()

                                if cant == 0:  # No hay ningun dispositivo cargado en el archivo.
                                    nombre = 'Evento {0}'.format((cant + 1))
                                else:
                                    nombre = (listaEventos.item(cant - 1)).text()
                                    numero = int(nombre[len('Evento'):])
                                    numero = str(numero + 1)
                                    nombre = nombre[0:len('Evento')] + ' ' + numero

                                    # Agrega el evento a la lista
                                item = QtWidgets.QListWidgetItem()
                                item.setText(nombre)
                                listaEventos.addItem(item)

                                # Habilita el boton por las dudas.
                                args.removerEventoTab1.setDisabled(False)
                                listaEventos.setCurrentRow(cant)
                                self.modificado = True  # Cada vez que se hace un cambio se actualiza este flag
                                break
                        break
                break

        # # Se habilitan los botones por las dudas (deshabilitan las funciones que eliminan)
        # estado = False
        #
        # args.agregarEventoTab1.setDisabled(estado)
        # # args.listaEventosTab4.setDisabled(estado)
        # args.comboBox1Tab1.setDisabled(estado)
        # args.spinBox1Tab1.setDisabled(estado)
        # args.spinBox2Tab1.setDisabled(estado)
        # args.comboBox2Tab1.setDisabled(estado)
        self.__setDisabledConfig(listaBotones, listaEventos, args)

    # Agrega un boton en Configuracion Placas BAP3 tab 4
    def agregarBoton(self, listaBAP3, listaBotones, listaEventos, args):
        # print('agregarBoton')
        rutaImagenBoton, tipos = QFileDialog.getOpenFileName(self, 'Abrir imagen', 'resources/', 'Image Files (*.png *.jpg *.bmp)')   # Ruta del archivo imagen

        if not rutaImagenBoton:
            return

        self.modificado = True  # Cada vez que se hace un cambio se actualiza este flag

        selBAP3 = listaBAP3.currentRow()
        posBAP3 = self.__findPosBAP(selBAP3, 'BAP3')

        nombreImagenBoton = self.__getNombreImagenBoton(rutaImagenBoton)    # Obtiene el nombre del archivo imagen

        for i in range(len(self.root[posBAP3])):
            if self.root[posBAP3][i].tag == 'Botones':
                if len(self.root[posBAP3][i]) == 0:
                    listaBotones.clear()    # En el caso de que la lista tenga los botones cargados en Configuration

                boton = self.__botonGen(self.root[posBAP3][i], nombreImagenBoton)
                self.root[posBAP3][i].append(boton)

                cant = listaBotones.count()

                if cant == 0:  # No hay ningun dispositivo en la lista.
                    nombre = 'Boton {0}:'.format((cant + 1))
                else:
                    nombre = (listaBotones.item(cant - 1)).text()
                    numero = int(nombre[len('Boton'):nombre.find(':')])
                    numero = str(numero + 1)
                    nombre = nombre[0:len('Boton')] + ' ' + numero + ':'

                item = QtWidgets.QListWidgetItem()
                item.setText(nombre)
                # item.setToolTip(nombreImagenBoton)
                listaBotones.addItem(item)
                listaBotones.setCurrentRow(cant)
                break
            elif i == len(self.root[posBAP3])-1:    # Se recorrieron tods los tags y no esta 'Botones'
                botones = self.__botonesGen(self.root[posBAP3], nombreImagenBoton)    # Crea tag botones generico
                self.root[posBAP3].insert(0, botones)   # Se agrega el tag 'Botones' a la BAP3 al principio de la lista
                self.cargarBotones(listaBAP3, listaBotones, listaEventos, args)

        # Se habilitan los botones por las dudas (deshabilitan las funciones que eliminan)
        estado = False
        args.removerBotonTab4.setDisabled(estado)
        args.agregarEventoTab4.setDisabled(estado)
        args.listaEventosTab4.setDisabled(estado)
        args.comboBox1Tab4.setDisabled(estado)
        args.spinBox1Tab4.setDisabled(estado)
        args.spinBox2Tab4.setDisabled(estado)
        args.comboBox2Tab4.setDisabled(estado)

    # Boton agregar Evento tab 4
    def agregarEvento(self, listaBAP3, listaBotones, listaEventos, args):
        # print('agregarEvento')
        self.modificado = True  # Cada vez que se hace un cambio se actualiza este flag

        selBAP3 = listaBAP3.currentRow()
        numBoton = listaBotones.currentRow()
        cant = listaEventos.count()

        posBAP3 = self.__findPosBAP(selBAP3, 'BAP3')

        for i in range(len(self.root[posBAP3])):  # Todos los tags dentro de la BAP seleccionada.
            if self.root[posBAP3][i].tag == 'Botones':
                for j in range(len(self.root[posBAP3][i][numBoton])):
                    if self.root[posBAP3][i][numBoton][j].tag == 'Eventos':

                        # Cuando se agrega un nuevo evento se mantiene como referencia el ultimo de la lista.
                        if cant == 0:  # No hay ningun dispositivo cargado en el archivo.
                            nombre = 'Evento {0}'.format((cant + 1))
                        else:
                            nombre = (listaEventos.item(cant - 1)).text()
                            numero = int(nombre[len('Evento'):])
                            numero = str(numero + 1)
                            nombre = nombre[0:len('Evento')] + ' ' + numero

                        # Agrega el evento a la lista
                        item = QtWidgets.QListWidgetItem()
                        item.setText(nombre)
                        listaEventos.addItem(item)

                        evento = self.__eventoGen(self.root[posBAP3][i][numBoton][j])   # Crea un evento
                        self.root[posBAP3][i][numBoton][j].append(evento)   # Agrega el evento al archivo .dat
                        listaEventos.setCurrentRow(cant)

                        # Habilita el boton por las dudas.
                        args.removerEventoTab4.setDisabled(False)
                        break

        # Se habilitan los botones por las dudas (deshabilitan las funciones que eliminan)
        estado = False

        args.listaEventosTab4.setDisabled(estado)
        args.removerEventoTab4.setDisabled(estado)
        args.comboBox1Tab4.setDisabled(estado)
        args.spinBox1Tab4.setDisabled(estado)
        args.spinBox2Tab4.setDisabled(estado)
        args.comboBox2Tab4.setDisabled(estado)

        args.comboBox1Tab4.setVisible(not estado)
        args.spinBox1Tab4.setVisible(not estado)
        args.spinBox2Tab4.setVisible(not estado)
        args.comboBox2Tab4.setVisible(not estado)

        args.labelAccionTab4.setVisible(not estado)
        args.labelSalidaTab4.setVisible(not estado)
        args.labelTiempoTab4.setVisible(not estado)
        args.labelRtaOKTab4.setVisible(not estado)

        # listaEventos.setCurrentRow(cant)

    # Boton remover. Elimina los dispositivos de cada lista.
    def removerDisp(self, lista, configgroupbox, removerbutton, tipoBAP='BAP2'):
        # print('removerDisp')

        seldispositivo = lista.currentRow()

        posdispositivo = self.__findPosBAP(seldispositivo, tipoBAP)

        mensaje = QMessageBox()
        mensaje.setText('¿Está seguro de que desea eliminar este dispositivo?')
        mensaje.setWindowTitle('Eliminar dispositivo')
        eliminarButton = mensaje.addButton('Si', mensaje.YesRole)
        noeliminarButton = mensaje.addButton('No', mensaje.NoRole)
        mensaje.exec_()

        if mensaje.clickedButton() == eliminarButton:
            lista.takeItem(seldispositivo)     # Borra el dispositivo de la lista.

            child = self.root.getchildren()[posdispositivo]
            self.root.remove(child)
            self.modificado = True  # Cada vez que se hace un cambio se actualiza este flag

        # Cuando no hay dispositivos cargados, se deshabilita el panel derecho y el boton remover.
        if lista.count() == 0:
            removerbutton.setDisabled(True)
            configgroupbox.setDisabled(True)

    # Elimina el boton seleccionado en tab1
    def removerBotonConfig(self, listaBotones, listaEventos, args):
        selBoton = listaBotones.currentRow()

        if selBoton == -1:
            return

        for i in range(len(self.root)):
            if self.root[i].tag == 'Configuration':
                for j in range(len(self.root[i])):
                    if self.root[i][j].tag == 'Botones':
                        mensaje = QMessageBox()
                        mensaje.setText('¿Está seguro de que desea eliminar este boton?')
                        mensaje.setWindowTitle('Eliminar boton')
                        eliminarButton = mensaje.addButton('Si', mensaje.YesRole)
                        noeliminarButton = mensaje.addButton('No', mensaje.NoRole)
                        mensaje.exec_()

                        if mensaje.clickedButton() == eliminarButton:
                            listaBotones.takeItem(selBoton)  # Borra el dispositivo de la lista.

                            child = self.root[i][j].getchildren()[selBoton]
                            self.root[i][j].remove(child)
                            self.modificado = True  # Cada vez que se hace un cambio se actualiza este flag

                            if listaBotones.count() == 0:
                                listaEventos.clear()

                            break

        self.__setDisabledConfig(listaBotones, listaEventos, args)

    # Elimina el evento seleccionado en tab1
    def removerEventoConfig(self, listaBotones, listaEventos, args):
        selBoton = listaBotones.currentRow()
        selEvento = listaEventos.currentRow()

        if selBoton == -1 or selEvento == -1:
            return

        for i in range(len(self.root)):
            if self.root[i].tag == 'Configuration':
                for j in range(len(self.root[i])):
                    if self.root[i][j].tag == 'Botones':
                        for k in range(len(self.root[i][j][selBoton])):
                            if self.root[i][j][selBoton][k].tag == 'Eventos':
                                mensaje = QMessageBox()
                                mensaje.setText('¿Está seguro de que desea eliminar este evento?')
                                mensaje.setWindowTitle('Eliminar evento')
                                eliminarButton = mensaje.addButton('Si', mensaje.YesRole)
                                noeliminarButton = mensaje.addButton('No', mensaje.NoRole)
                                mensaje.exec_()

                                if mensaje.clickedButton() == eliminarButton:
                                    listaEventos.takeItem(selEvento)  # Borra el dispositivo de la lista.

                                    child = self.root[i][j][selBoton][k].getchildren()[selEvento]
                                    self.root[i][j][selBoton][k].remove(child)
                                    self.modificado = True  # Cada vez que se hace un cambio se actualiza este flag
                                    break

        self.__setDisabledConfig(listaBotones, listaEventos, args)

    # Elimina Boton de Configuracion Placas BAP3 tab 4
    def removerBoton(self, listaBAP3, listaBotones, listaEventos, args):
        selBAP3 = listaBAP3.currentRow()
        selBoton = listaBotones.currentRow()

        if selBAP3 == -1 or selBoton == -1:
            return

        posBAP3 = self.__findPosBAP(selBAP3, 'BAP3')

        botones = True

        for i in range(len(self.root[posBAP3])):  # Todos los botones
            if self.root[posBAP3][i].tag == 'Botones':
                if len(self.root[posBAP3][i]) != 0:
                    if self.root[posBAP3][i][selBoton].tag == 'Boton':
                        mensaje = QMessageBox()
                        mensaje.setText('¿Está seguro de que desea eliminar este boton?')
                        mensaje.setWindowTitle('Eliminar boton')
                        eliminarButton = mensaje.addButton('Si', mensaje.YesRole)
                        noeliminarButton = mensaje.addButton('No', mensaje.NoRole)
                        mensaje.exec_()

                        if mensaje.clickedButton() == eliminarButton:
                            listaBotones.takeItem(selBoton)  # Borra el dispositivo de la lista.

                            child = self.root[posBAP3][i].getchildren()[selBoton]
                            self.root[posBAP3][i].remove(child)
                            self.modificado = True  # Cada vez que se hace un cambio se actualiza este flag

                            if listaBotones.count() == 0:
                                botones = False
                                self.loadDatConfig(args.listaTabs, listaBotones, listaEventos, args)

                            break

        self.__setDisabled(listaBAP3, listaBotones, listaEventos, botones, args)

    # Elimina Evento de Configuracion Placas BAP3 tab4
    def removerEvento(self, listaBAP3, listaBotones, listaEventos, args):
        selBAP3 = listaBAP3.currentRow()
        selBoton = listaBotones.currentRow()
        selEvento = listaEventos.currentRow()

        if selBAP3 == -1 or selBoton == -1 or selEvento == -1:
            return

        posBAP3 = self.__findPosBAP(selBAP3, 'BAP3')

        for i in range(len(self.root[posBAP3])):  # Todos los botones
            if self.root[posBAP3][i].tag == 'Botones':
                for j in range(len(self.root[posBAP3][i][selBoton])):
                    if self.root[posBAP3][i][selBoton][j].tag == 'Eventos':
                        mensaje = QMessageBox()
                        mensaje.setText('¿Está seguro de que desea eliminar este evento?')
                        mensaje.setWindowTitle('Eliminar evento')
                        eliminarButton = mensaje.addButton('Si', mensaje.YesRole)
                        noeliminarButton = mensaje.addButton('No', mensaje.NoRole)
                        mensaje.exec_()

                        if mensaje.clickedButton() == eliminarButton:
                            listaEventos.takeItem(selEvento)  # Borra el dispositivo de la lista.

                            child = self.root[posBAP3][i][selBoton][j].getchildren()[selEvento]
                            self.root[posBAP3][i][selBoton][j].remove(child)
                            self.modificado = True  # Cada vez que se hace un cambio se actualiza este flag
                            break

        if listaEventos.count() == 0:
            # Se habilitan los botones por las dudas (deshabilitan las funciones que eliminan)
            estado = True

            # args.listaEventosTab4.setDisabled(estado)
            args.removerEventoTab4.setDisabled(estado)
            # args.comboBox1Tab4.setDisabled(estado)
            # args.spinBox1Tab4.setDisabled(estado)
            # args.spinBox2Tab4.setDisabled(estado)
            # args.comboBox2Tab4.setDisabled(estado)

            args.comboBox1Tab4.setVisible(not estado)
            args.spinBox1Tab4.setVisible(not estado)
            args.spinBox2Tab4.setVisible(not estado)
            args.comboBox2Tab4.setVisible(not estado)

            args.labelAccionTab4.setVisible(not estado)
            args.labelSalidaTab4.setVisible(not estado)
            args.labelTiempoTab4.setVisible(not estado)
            args.labelRtaOKTab4.setVisible(not estado)

    #  Habilita o deshabilita el panel derecho de configuracion. Atributo 'enabled'
    def habilitar(self, lista, checkbox, l1, l2, l3, l4, l5, l6, l7, tipoBAP='BAP2'):
        seldispositivo = lista.currentRow()

        posdispositivo = self.__findPosBAP(seldispositivo, tipoBAP)

        if checkbox.isChecked() is False:
            l1.setDisabled(True)
            l2.setDisabled(True)
            l3.setDisabled(True)
            l4.setDisabled(True)
            l5.setDisabled(True)
            l6.setDisabled(True)
            l7.setDisabled(True)

            self.root[posdispositivo].attrib['enabled'] = 'false'

        else:
            l1.setDisabled(False)
            l2.setDisabled(False)
            l3.setDisabled(False)
            l4.setDisabled(False)
            l5.setDisabled(False)
            l6.setDisabled(False)
            l7.setDisabled(False)

            self.root[posdispositivo].attrib['enabled'] = 'true'

        self.modificado = True  # Cada vez que se hace un cambio se actualiza este flag

    # Cada vez que se selecciona una placa BAP2 o BAP3 (Solo tab 3), Consola o Kant de la lista (mouse o tecla)
    def cargarItem(self, lista, checkbox, removerbutton, l1, l2, l3, l4, l5, l6, l7, OutsNum=None, tipoBAP='BAP2'):
        removerbutton.setDisabled(False)    # TODO: REVISAR COMO SACAR ESTO
        seldispositivo = lista.currentRow()  # Posicion en la lista del dispositivo seleccionado

        if seldispositivo == -1:
            return

        lineas = []

        labels = ['NroSucursal',
                  'NombreSucursal',
                  'NombreConsola',
                  'NombreKant',
                  'InfoExtra',
                  'IP',
                  'IP_Port',
                  'NroNodoKANT',
                  'NroAbonadoKANT',
                  'IDPlaca',
                  'AliveFrequency',
                  'RetryFrequency']

        posdispositivo = self.__findPosBAP(seldispositivo, tipoBAP)

        for label in labels:
            for i in range(len(self.root[posdispositivo])):
                if label == self.root[posdispositivo][i].tag:
                    lineas.append(self.root[posdispositivo][i].text)

        enabled = self.root[posdispositivo].attrib['enabled']

        if tipoBAP == 'BAP3':
            try:
                outsnum = self.root[posdispositivo].attrib['OutsNum']
            except KeyError:
                # Agrega la entrada 'OutsNum'
                self.root[posdispositivo].attrib['OutsNum'] = '0'  # Valor por defecto?
                outsnum = '0'

            OutsNum.setValue(int(outsnum))

        if self.dispositivo is 'Kant':
            linea1 = self.root[posdispositivo].attrib['nronodo']
        else:
            linea1 = self.root[posdispositivo].attrib['id']

        # Cuando se borra el ultimo elemento
        if posdispositivo < 0:
            l1.setText('')
            l2.setText('')
            l3.setText('')
            l4.setText('')
            l5.setText('')
            l6.setText('')
            l7.setText('')
        else:
            try:    # No todos los dispositivos tienen la misma cantidad de lineas de configuracion.
                l1.setText(linea1)
                l2.setText(lineas[0])
                l3.setText(lineas[1])
                l4.setText(lineas[2])
                l5.setText(lineas[3])
                l6.setText(lineas[4])
                l7.setText(lineas[5])
            except IndexError:
                pass

        if enabled == 'true':
            checkbox.setChecked(True)
        else:
            checkbox.setChecked(False)

    # Carga los eventos disponibles cuando se selecciona un boton en el tab 1
    def cargarEventosConfig(self, listaBotones, listaEventos, args):
        selBoton = listaBotones.currentRow()
        listaEventos.setCurrentRow(0)  # Se resetea la seleccion sino puede quedar seteado del boton anterior.
        listaEventos.clear()

        # Configuration = self.root.findall('Configuration')
        # Configuration.get('Botones')

        for i in range(len(self.root)):
            if self.root[i].tag == 'Configuration':
                for j in range(len(self.root[i])):
                    if self.root[i][j].tag == 'Botones':
                        if len(self.root[i][j]) != 0:
                            for k in range(len(self.root[i][j][selBoton])):
                                if self.root[i][j][selBoton][k].tag == 'Eventos':
                                    if len(self.root[i][j][selBoton][k]) != 0:
                                        for m in range(len(self.root[i][j][selBoton][k])):
                                            cant = listaEventos.count()
                                            item = QtWidgets.QListWidgetItem()
                                            item.setText('Evento {0}'.format(cant + 1))
                                            listaEventos.addItem(item)
                                            listaEventos.setCurrentRow(0)
                                        break
                                    else:
                                        break

        self.__setDisabledConfig(listaBotones, listaEventos, args)

    # Carga el evento seleccionado en el tab 1. El parametro tab1 es para poder cargar datos en tab1 o tab4.
    def cargarEventoConfig(self, listaBotones, listaEventos, args, tab1=True):
        selBoton = listaBotones.currentRow()
        selEvento = listaEventos.currentRow()

        if selBoton == -1 or selEvento == -1:
            return

        for i in range(len(self.root)):
            if self.root[i].tag == 'Configuration':
                for j in range(len(self.root[i])):
                    if self.root[i][j].tag == 'Botones':
                        if len(self.root[i][j]) != 0:
                            if self.root[i][j][selBoton].tag == 'Boton':
                                for k in range(len(self.root[i][j][selBoton])):
                                    if self.root[i][j][selBoton][k].tag == 'Eventos':
                                        if len(self.root[i][j][selBoton][k]) == 0:  # El boton no tiene eventos cargados.
                                            return
                                        elif self.root[i][j][selBoton][k][selEvento].tag == 'Evento':
                                            try:
                                                accion = self.root[i][j][selBoton][k][selEvento].attrib['Accion']
                                            except KeyError:
                                                accion = ''
                                            try:
                                                salida = self.root[i][j][selBoton][k][selEvento].attrib['Salida']
                                            except KeyError:
                                                salida = 0
                                            try:
                                                tiempo = self.root[i][j][selBoton][k][selEvento].attrib['Tiempo']
                                            except KeyError:
                                                tiempo = 0
                                            try:
                                                respuestaok = self.root[i][j][selBoton][k][selEvento].attrib['RespuestaOK']
                                            except KeyError:
                                                respuestaok = ''

                                            # Modifica tab1
                                            if tab1 is True:
                                                args.comboBox1Tab1.setCurrentText(accion)
                                                args.spinBox1Tab1.setValue(int(salida))
                                                args.spinBox2Tab1.setValue(int(tiempo))
                                                args.comboBox2Tab1.setCurrentText(respuestaok)
                                            # Modifica tab4 cuando carga los botones por defecto de Configuration.
                                            else:
                                                args.comboBox1Tab4.setCurrentText(accion)
                                                args.spinBox1Tab4.setValue(int(salida))
                                                args.spinBox2Tab4.setValue(int(tiempo))
                                                args.comboBox2Tab4.setCurrentText(respuestaok)
                                            return

    # Cuando se selecciona una BAP3 de la lista del tab 4
    def cargarBotones(self, listaBAP3, listaBotones, listaEventos, args):
        listaBotones.setCurrentRow(0)   # Por si la BAP actual tiene menos botones que la BAP selecionada anteriormente.
        listaBotones.clear()
        listaEventos.clear()

        selBAP3 = listaBAP3.currentRow()  # Posicion en la lista de la BAP3 seleccionada

        if selBAP3 == -1:
            return

        posBAP3 = self.__findPosBAP(selBAP3, 'BAP3')

        botones = False

        for i in range(len(self.root[posBAP3])):
            if self.root[posBAP3][i].tag == 'Botones':
                if len(self.root[posBAP3][i]) != 0:
                    botones = True  # El tag Botones contiene elementos.
                    for j in range(len(self.root[posBAP3][i])):
                        cant = listaBotones.count()
                        item = QtWidgets.QListWidgetItem()
                        item.setFlags(int(item.flags()) | QtCore.Qt.ItemIsEditable)
                        listaBotones.addItem(item)
                        try:
                            nombre = 'Boton {0}: {1}'.format(cant + 1, self.root[posBAP3][i][j].attrib['id'])
                        except KeyError:
                            nombre = 'Boton {0}'.format(cant+1)

                        item.setText(nombre)

                        # Crea el tooltip con el nombre del icono elegido para cada boton.
                        for k in range(len(self.root[posBAP3][i][j])):
                            if self.root[posBAP3][i][j][k].tag == 'Icon':
                                for m in range(len(self.root[posBAP3][i][j][k])):
                                    if self.root[posBAP3][i][j][k][m].tag == 'Boton':
                                        nombreImagenBoton = self.root[posBAP3][i][j][k][m].text

                                        tooltip = self.__getNombreImagenBoton(nombreImagenBoton)
                                        item.setToolTip(tooltip)
                                        break
                                break
                # Esta el tag Botones pero no contiene elementos.
                else:
                    # Si la BAP3 seleccionada no contiene botones, se cargan los botones del tag "Configuration"
                    self.loadDatConfig(args.listaTabs, args.listaBotonesTab4, args.listaEventosTab4, args, itemEdit=False)
                    break

        self.__setDisabled(listaBAP3, listaBotones, listaEventos, botones, args)

        listaBotones.setCurrentRow(0)

    # Carga todos los eventos cuando se selecciona un boton de la lista del tab 4
    def cargarEventos(self, listaBAP3, listaBotones, listaEventos, args):
        selBAP3 = listaBAP3.currentRow()
        numBoton = listaBotones.currentRow()
        listaEventos.setCurrentRow(0)   # Se resetea la seleccion sino puede quedar seteado del boton anterior.
        listaEventos.clear()

        botones = False
        eventos = False

        # Encuentra la BAP3 seleccionada.
        posBAP3 = self.__findPosBAP(selBAP3, 'BAP3')

        for i in range(len(self.root[posBAP3])):  # Todos los botones
            if self.root[posBAP3][i].tag == 'Botones':
                if len(self.root[posBAP3][i]) != 0:     # Hay botones cargados en la BAP3?
                    botones = True  # Hay botones cargados.
                    for j in range(len(self.root[posBAP3][i][numBoton])):
                        if self.root[posBAP3][i][numBoton][j].tag == 'Eventos':
                            # if len(self.root[posBAP3][i][numBoton][j]) != 0:
                                # eventos = True
                            for k in range(len(self.root[posBAP3][i][numBoton][j])):
                                cant = listaEventos.count()
                                item = QtWidgets.QListWidgetItem()
                                item.setText('Evento {0}'.format(cant + 1))
                                listaEventos.addItem(item)
                            break
                    break
                else:   # Existe el tag 'Botones' pero no hay botones cargados en la BAP3
                    self.cargarEventosConfig(args.listaBotonesTab4, args.listaEventosTab4, args)
                    break

        self.__setDisabled(listaBAP3, listaBotones, listaEventos, botones, args)

        listaEventos.setCurrentRow(0)

    # Carga el evento de la lista seleccionado tab 4
    def cargarEvento(self, listaBAP3, listaBotones, listaEventos, args):
        selBAP3 = listaBAP3.currentRow()
        selBoton = listaBotones.currentRow()
        selEvento = listaEventos.currentRow()

        if selBAP3 == -1 or selBoton == -1 or selEvento == -1:
            return

        botones = False
        eventos = False

        posBAP3 = self.__findPosBAP(selBAP3, 'BAP3')

        for i in range(len(self.root[posBAP3])):  # Todos los elementos dentro de la BAP
            if self.root[posBAP3][i].tag == 'Botones':
                if len(self.root[posBAP3][i]) != 0:  # Hay botones cargados.
                    botones = True
                    for j in range(len(self.root[posBAP3][i][selBoton])):   # Todos los elementos dentro de cada boton.
                        if self.root[posBAP3][i][selBoton][j].tag == 'Eventos':
                            if len(self.root[posBAP3][i][selBoton][j]) != 0:    # El boton no tiene eventos cargados.
                                # break
                                try:
                                    accion = self.root[posBAP3][i][selBoton][j][selEvento].attrib['Accion']
                                except KeyError:
                                    accion = ''
                                try:
                                    salida = self.root[posBAP3][i][selBoton][j][selEvento].attrib['Salida']
                                except KeyError:
                                    salida = 0
                                try:
                                    tiempo = self.root[posBAP3][i][selBoton][j][selEvento].attrib['Tiempo']
                                except KeyError:
                                    tiempo = 0
                                try:
                                    respuestaok = self.root[posBAP3][i][selBoton][j][selEvento].attrib['RespuestaOK']
                                except KeyError:
                                    respuestaok = ''

                                args.comboBox1Tab4.setCurrentText(accion)
                                args.spinBox1Tab4.setValue(int(salida))
                                args.spinBox2Tab4.setValue(int(tiempo))
                                args.comboBox2Tab4.setCurrentText(respuestaok)
                                break
                            # No hay eventos cargados en el boton
                            else:
                                break
                # No hay botones cargados en la BAP
                else:
                    # Si no hay botones cargados o no existe el tag, debe cargar los botones y eventos de Configuration.
                    self.cargarEventoConfig(args.listaBotonesTab4, args.listaEventosTab4, args, tab1=False)
                    break

    # Setea las propiedades de cada evento cuando se modifican desde la GUI tab 1
    def setEventoConfig(self, listaBotones, listaEventos, args):
        # print('setEventoConfig')
        self.modificado = True
        selBoton = listaBotones.currentRow()
        selEvento = listaEventos.currentRow()

        if selBoton == -1 or selEvento == -1:
            return

        for i in range(len(self.root)):
            if self.root[i].tag == 'Configuration':
                for j in range(len(self.root[i])):
                    if self.root[i][j].tag == 'Botones':
                        if self.root[i][j][selBoton].tag == 'Boton':
                            for k in range(len(self.root[i][j][selBoton])):
                                if self.root[i][j][selBoton][k].tag == 'Eventos':
                                    if len(self.root[i][j][selBoton][k]) == 0:  # El boton no tiene eventos cargados.
                                        return
                                    elif self.root[i][j][selBoton][k][selEvento].tag == 'Evento':
                                        try:
                                            self.root[i][j][selBoton][k][selEvento].attrib['Accion'] = args.comboBox1Tab1.currentText()
                                        except KeyError:
                                            pass
                                        try:
                                            self.root[i][j][selBoton][k][selEvento].attrib[
                                                'Salida'] = args.spinBox1Tab1.text()
                                        except KeyError:
                                            pass
                                        try:
                                            self.root[i][j][selBoton][k][selEvento].attrib[
                                                'Tiempo'] = args.spinBox2Config.text()
                                        except KeyError:
                                            pass
                                        try:
                                            self.root[i][j][selBoton][k][selEvento].attrib[
                                                'RespuestaOK'] = args.comboBox2Tab1.currentText()
                                        except KeyError:
                                            pass

    # Setea los parametros del evento seleccionado
    def setEvento(self, listaBAP3, listaBotones, listaEventos, args):
        # print('setEvento')
        self.modificado = True
        selBAP3 = listaBAP3.currentRow()
        selBoton = listaBotones.currentRow()
        selEvento = listaEventos.currentRow()

        if selBAP3 == -1 or selBoton == -1 or selEvento == -1:
            return

        posBAP3 = self.__findPosBAP(selBAP3, 'BAP3')

        for i in range(len(self.root[posBAP3])):  # Todos los elementos dentro de la BAP
            if self.root[posBAP3][i].tag == 'Botones':
                if len(self.root[posBAP3][i]) != 0:  # Hay botones cargados.
                    for j in range(len(self.root[posBAP3][i][selBoton])):  # Todos los elementos dentro de cada boton.
                        if self.root[posBAP3][i][selBoton][j].tag == 'Eventos':
                            if len(self.root[posBAP3][i][selBoton][j]) == 0:  # El boton no tiene eventos cargados.
                                break
                            try:
                                self.root[posBAP3][i][selBoton][j][selEvento].attrib['Accion'] = args.comboBox1Tab4.currentText()
                            except KeyError:
                                pass
                            try:
                                self.root[posBAP3][i][selBoton][j][selEvento].attrib['Salida'] = args.spinBox1Tab4.text()
                            except KeyError:
                                pass
                            try:
                                self.root[posBAP3][i][selBoton][j][selEvento].attrib['Tiempo'] = args.spinBox2Tab4.text()
                            except KeyError:
                                pass
                            try:
                                self.root[posBAP3][i][selBoton][j][selEvento].attrib['RespuestaOK'] = args.comboBox2Tab4.currentText()
                            except KeyError:
                                pass

    # Cambio de id tabs tab 1
    def setIdTabsConfig(self, listaTabs):
        # print('setIdTabsConfig')
        selTab = listaTabs.currentRow()
        item = listaTabs.item(selTab)

        if selTab == -1:
            return

        for i in range(len(self.root)):
            if self.root[i].tag == 'Configuration':
                for j in range(len(self.root[i])):
                    if self.root[i][j].tag == 'Tabs':
                        self.root[i][j][selTab].attrib['id'] = item.text()
                        self.modificado = True
                        return

    # Cambio de id en botones del tab 1
    def setIdBotonesConfig(self, listaBotones):
        # print('setIdBotonesConfig')
        selBoton = listaBotones.currentRow()
        item = listaBotones.item(selBoton)

        if selBoton == -1:
            return

        txtBoton = 'Boton ' + str(selBoton + 1) + ': '

        for i in range(len(self.root)):
            if self.root[i].tag == 'Configuration':
                for j in range(len(self.root[i])):
                    if self.root[i][j].tag == 'Botones':
                        txt = item.text()
                        if txt.find('Boton') is not -1 and txt.find(':') is not -1:
                            item.setText(txt)
                            self.root[i][j][selBoton].attrib['id'] = txt[txt.find(':') + 2:]
                            self.modificado = True
                            return
                        else:
                            txtBoton = txtBoton + txt
                            item.setText(txtBoton)
                            self.root[i][j][selBoton].attrib['id'] = txt
                            self.modificado = True
                            return

    # Cambio de id en botones del tab 4
    def setIdBotones(self, listaBAP3, listaBotones):
        # print('setIdBotones')
        selBAP3 = listaBAP3.currentRow()
        selBoton = listaBotones.currentRow()
        item = listaBotones.item(selBoton)

        if selBAP3 == -1 or selBoton == -1:
            return

        posBAP3 = self.__findPosBAP(selBAP3, 'BAP3')

        txtBoton = 'Boton ' + str(selBoton + 1) + ': '

        for i in range(len(self.root[posBAP3])):
            if self.root[posBAP3][i].tag == 'Botones':
                txt = item.text()
                if txt.find('Boton') is not -1 and txt.find(':') is not -1:
                    item.setText(txt)
                    self.root[posBAP3][i][selBoton].attrib['id'] = txt[txt.find(':')+2:]
                    self.modificado = True
                    return
                else:
                    txtBoton = txtBoton + txt
                    item.setText(txtBoton)
                    self.root[posBAP3][i][selBoton].attrib['id'] = txt
                    self.modificado = True
                    return

    # Setea OutsNum de Configuration en tab 1
    def setOutsNumConfig(self, spinBoxOutsNum):
        # print('setOutsNumConfig')

        outsnum = spinBoxOutsNum.text()

        for i in range(len(self.root)):
            if self.root[i].tag == 'Configuration':
                for j in range(len(self.root[i])):
                    if self.root[i][j].tag == 'BAP3':
                        self.root[i][j].attrib['OutsNum'] = outsnum
                        self.modificado = True
                        return

    # Setea OutsNum de las BAP3 tab 3
    def setOutsNumBAP3(self, listaBAP3, spinBoxOutsNumBAP3):
        # print('setOutsNumBAP3')
        self.modificado = True

        selBAP3 = listaBAP3.currentRow()  # Posicion en la lista de la BAP3 seleccionada

        if selBAP3 == -1:
            return

        outsnum = spinBoxOutsNumBAP3.text()

        posBAP3 = self.__findPosBAP(selBAP3, 'BAP3')

        self.root[posBAP3].attrib['OutsNum'] = outsnum

    # Metodo para cambiar entre la configuracion por defecto y la configuracion particular de las BAP3. No se usa.
    def configToBAP(self, args):
        if args.checkBoxPlacas.isChecked() is True:
            self.loadDatConfig(args.listaTabs, args.listaBotones, args)
        else:
            self.cargarBotones(args.listaBAP3Tab4, args.listaBotones, args.listaEventosTab4, args)

    # Boton guardar de todas los tabs
    def guardarCambios(self):
        # print('guardarCambios')

        self.modificado = False
        self.tree.write(self.filename, pretty_print=True, xml_declaration=True, encoding='utf-8')

    def crearBackup(self, carpeta):
        try:
            os.mkdir(carpeta)
        except FileExistsError:
            pass

        shutil.copy(self.filename, carpeta)

    # @staticmethod   # Este metodo no usa self entonces se puede declarar static y sacarle el self.
    def borrarBackup(self, carpeta):
        try:
            shutil.rmtree(carpeta)
        except FileNotFoundError:
            pass

    # Se actualiza tab 4 cuando se lo selecciona.
    def updateTab(self, tabs, listaBAP3, listaBotones, listaEventos, args):
        # Si se agrega un boton en tab 1 el cambio se debe ver reflejado en el tab 4 automaticamente.
        if tabs.currentIndex() == 3:
            self.loadDat(listaBAP3, None, None, 'BAP3', args)

    # Mapea las BAP2 y BAP3 de la lista de seleccion a la posicion real en el archivo .dat
    def __findPosBAP(self, selBAP, tipoBAP):
        # print('__findPosBAP')
        posBAP = 0

        # filtra de acuerdo a tipoBAP
        if self.dispositivo == 'BAP':
            for i in range(len(self.root)):
                try:
                    if self.root[i].attrib['TipoPlaca'] == tipoBAP:
                        if selBAP == posBAP:
                            posBAP = i
                            return posBAP
                        else:
                            posBAP += 1
                except KeyError:
                    continue
            return selBAP   # Si no encuentra ninguna BAP
        else:
            return selBAP   # Si no es una BAP devuelve la posicion sin cambios

    # Encapsula la creacion de un boton generico.
    def __botonGen(self, ruta, nombreImagenBoton):
        boton = etree.SubElement(ruta, 'Boton', attrib={'id': ''})
        etree.SubElement(boton, 'Caption')
        icon = etree.SubElement(boton, 'Icon')
        etree.SubElement(boton, 'Eventos')

        botonen = etree.SubElement(icon, 'Boton')
        botonen.text = 'Resources\{0}.png'.format(nombreImagenBoton)
        botondi = etree.SubElement(icon, 'BotonDisabled')
        botondi.text = 'Resources\{0}_Disabled.png'.format(nombreImagenBoton)
        disparo = etree.SubElement(icon, 'Disparo')
        disparo.text = 'Resources\BotonFlotante_v4_Verde_Disparo_{0}.png'.format(nombreImagenBoton)
        ok = etree.SubElement(icon, 'OK')
        ok.text = 'Resources\BotonFlotante_v4_Verde_DisparoOK_{0}.png'.format(nombreImagenBoton)
        error = etree.SubElement(icon, 'Error')
        error.text = 'Resources\BotonFlotante_v4_Rojo_DisparoError_{0}.png'.format(nombreImagenBoton)
        nack = etree.SubElement(icon, 'NACK')
        nack.text = 'Resources\BotonFlotante_v4_NACK_Disparo_{0}.png'.format(nombreImagenBoton)

        return boton

    def __botonesGen(self, ruta, nombreImagenBoton):
        botones = etree.SubElement(ruta, 'Botones')
        boton = etree.SubElement(botones, 'Boton', attrib={'id': ''})
        caption = etree.SubElement(boton, 'Caption')
        icon = etree.SubElement(boton, 'Icon')
        eventos = etree.SubElement(boton, 'Eventos')

        botonen = etree.SubElement(icon, 'Boton')
        botonen.text = 'Resources\{0}.png'.format(nombreImagenBoton)
        botondi = etree.SubElement(icon, 'BotonDisabled')
        botondi.text = 'Resources\{0}_Disabled.png'.format(nombreImagenBoton)
        disparo = etree.SubElement(icon, 'Disparo')
        disparo.text = 'Resources\BotonFlotante_v4_Verde_Disparo_{0}.png'.format(nombreImagenBoton)
        ok = etree.SubElement(icon, 'OK')
        ok.text = 'Resources\BotonFlotante_v4_Verde_DisparoOK_{0}.png'.format(nombreImagenBoton)
        error = etree.SubElement(icon, 'Error')
        error.text = 'Resources\BotonFlotante_v4_Rojo_DisparoError_{0}.png'.format(nombreImagenBoton)
        nack = etree.SubElement(icon, 'NACK')
        nack.text = 'Resources\BotonFlotante_v4_NACK_Disparo_{0}.png'.format(nombreImagenBoton)

        return botones

    # Encapsula la creacion de un evento generico.
    def __eventoGen(self, ruta):
        # Valores por defecto cualquiera.
        evento = etree.SubElement(ruta, 'Evento', attrib={'Accion': 'PULSAR', 'Salida': '1', 'Tiempo': '0', 'RespuestaOK': 'PULSADA'})
        return evento

    # Obtiene el nombre del archivo imagen que se usa como icono de boton nuevo
    def __getNombreImagenBoton(self, rutaBotonImagen):
        rutaBotonImagen = rutaBotonImagen.replace('\\', '/')

        try:
            extIndex = rutaBotonImagen[::-1].index('.')
            nameIndex = rutaBotonImagen[::-1].index('/', extIndex)
            return rutaBotonImagen[len(rutaBotonImagen)-nameIndex:len(rutaBotonImagen)-extIndex-1]
        except ValueError:
            return None

    # Habilita o deshabilita componentes de acuerdo a la configuracion del Tab 1
    def __setDisabledConfig(self, listaBotones, listaEventos, args):
        if listaBotones.count() == 0:
            estado = True

            listaEventos.clear()
            listaEventos.setDisabled(estado)

            args.agregarEventoTab1.setDisabled(estado)
            args.removerEventoTab1.setDisabled(estado)
            args.removerBotonTab1.setDisabled(estado)

        else:
            if listaEventos.count() == 0:
                estado = True
            else:
                estado = False

            listaEventos.setDisabled(False)

            args.agregarEventoTab1.setDisabled(False)
            args.removerEventoTab1.setDisabled(estado)
            args.removerBotonTab1.setDisabled(False)

        args.comboBox1Tab1.setDisabled(estado)
        args.spinBox1Tab1.setDisabled(estado)
        args.spinBox2Tab1.setDisabled(estado)
        args.comboBox2Tab1.setDisabled(estado)

        args.comboBox1Tab1.setVisible(not estado)
        args.spinBox1Tab1.setVisible(not estado)
        args.spinBox2Tab1.setVisible(not estado)
        args.comboBox2Tab1.setVisible(not estado)

        args.labelAccionTab1.setVisible(not estado)
        args.labelSalidaTab1.setVisible(not estado)
        args.labelTiempoTab1.setVisible(not estado)
        args.labelRtaOKTab1.setVisible(not estado)

    # Habilita o deshabilita componentes de acuerdo a la configuracion del Tab 4
    def __setDisabled(self, listaBAP3, listaBotones, listaEventos, botones, args):
        estado = None

        if listaBAP3.count() == 0:
            estado = True

            # Cuando no hay BAP3 cargadas no puede haber Botones ni Eventos
            args.listaEventosTab4.clear()
            args.listaBotonesTab4.clear()

            listaBAP3.setDisabled(estado)
            args.listaBotonesTab4.setDisabled(estado)
            # args.listaEventosTab4.setDisabled(estado)

            args.removerBotonTab4.setDisabled(estado)
            args.agregarBotonTab4.setDisabled(estado)
            args.removerEventoTab4.setDisabled(estado)
            args.agregarEventoTab4.setDisabled(estado)

        if listaBAP3.count() != 0:
            estado = False

            listaBAP3.setDisabled(estado)
            args.listaBotonesTab4.setDisabled(estado)
            args.agregarBotonTab4.setDisabled(estado)

        # La BAP3 no tiene botones propios
        if botones is False:
            if listaEventos.count() == 0:
                estado = True
            else:
                estado = False

            listaEventos.setDisabled(estado)

            args.agregarEventoTab4.setDisabled(True)
            args.removerEventoTab4.setDisabled(True)
            args.removerBotonTab4.setDisabled(True)

            args.comboBox1Tab4.setDisabled(True)
            args.spinBox1Tab4.setDisabled(True)
            args.spinBox2Tab4.setDisabled(True)
            args.comboBox2Tab4.setDisabled(True)

        # Si hay botones cargados en la BAP3
        elif botones is True:
            if listaEventos.count() == 0:
                estado = True
            else:
                estado = False

            args.agregarEventoTab4.setDisabled(False)
            args.removerEventoTab4.setDisabled(estado)
            args.removerBotonTab4.setDisabled(False)

            args.comboBox1Tab4.setDisabled(estado)
            args.spinBox1Tab4.setDisabled(estado)
            args.spinBox2Tab4.setDisabled(estado)
            args.comboBox2Tab4.setDisabled(estado)

        args.comboBox1Tab4.setVisible(not estado)
        args.spinBox1Tab4.setVisible(not estado)
        args.spinBox2Tab4.setVisible(not estado)
        args.comboBox2Tab4.setVisible(not estado)

        args.labelAccionTab4.setVisible(not estado)
        args.labelSalidaTab4.setVisible(not estado)
        args.labelTiempoTab4.setVisible(not estado)
        args.labelRtaOKTab4.setVisible(not estado)
