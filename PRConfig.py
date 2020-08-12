from PRConfig_ui import *
from PRConfig_model import Model
from datetime import datetime


# Clase que representa al controlador dentro del esquema Model-View-Controller
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        labelsBAP = ['NroSucursal', 'NombreSucursal', 'InfoExtra', 'IP_Port', 'NroAbonadoKANT', 'IDPlaca']
        labelsBAP3 = ['Tabs', 'Botones', 'NroSucursal', 'NombreSucursal', 'InfoExtra', 'IP_Port', 'NroAbonadoKANT', 'IDPlaca']
        labelsCON = ['NombreConsola', 'InfoExtra', 'IP', 'NroNodoKANT']
        labelsKAN = ['NombreKant', 'IP_Port', 'AliveFrequency', 'RetryFrequency']

        self.setupUi(self)

        self.FileNameBAP = 'BAPInfoManager.dat'
        self.FileNameCON = 'ConsoleInfoManager.dat'
        self.FileNameKAN = 'KantsInfoManager.dat'
        self.FileNameSp1 = 'Spools_PRManager.config'

        # El nombre de la carpeta de backup lo define la fecha y la hora.
        self.fecha = datetime.now()
        self.carpeta = self.fecha.strftime('%Y%m%d-%H%M%S')

        # Crea el objeto Model que contiene los metodos a utilizar.
        self.ModelSP1 = Model(self.FileNameSp1, self.carpeta)
        self.ModelBAP = Model(self.FileNameBAP, self.carpeta)
        self.ModelKAN = Model(self.FileNameKAN, self.carpeta)
        self.ModelCON = Model(self.FileNameCON, self.carpeta)

        # TAB 1
        self.createConfigurationBAP3GroupBox()

        self.listaTabs.itemChanged.connect(lambda: self.ModelBAP.setIdTabsConfig(self.listaTabs))
        self.listaBotonesTab1.itemChanged.connect(lambda: self.ModelBAP.setIdBotonesConfig(self.listaBotonesTab1))

        self.agregarEventoTab1.clicked.connect(lambda: self.ModelBAP.agregarEventoConfig(self.listaBotonesTab1, self.listaEventosTab1, self))
        self.agregarBotonTab1.clicked.connect(lambda: self.ModelBAP.agregarBotonConfig(self.listaBotonesTab1, self.listaEventosTab1, self))
        self.removerEventoTab1.clicked.connect(lambda: self.ModelBAP.removerEventoConfig(self.listaBotonesTab1, self.listaEventosTab1, self))
        self.removerBotonTab1.clicked.connect(lambda: self.ModelBAP.removerBotonConfig(self.listaBotonesTab1, self))

        self.guardarTab1.clicked.connect(lambda: self.ModelBAP.guardarCambios())

        # Edita Accion
        self.comboBox1Tab1.activated.connect(lambda: self.ModelBAP.setEventoConfig(self.listaBotonesTab1, self.listaEventosTab1, self))
        # Edita Salida
        self.spinBox1Config.editingFinished.connect(lambda: self.ModelBAP.setEventoConfig(self.listaBotonesTab1, self.listaEventosTab1, self))
        # Edita Tiempo
        self.spinBox2Config.editingFinished.connect(lambda: self.ModelBAP.setEventoConfig(self.listaBotonesTab1, self.listaEventosTab1, self))
        # Edita RespuestaOK
        self.comboBox2Config.activated.connect(lambda: self.ModelBAP.setEventoConfig(self.listaBotonesTab1, self.listaEventosTab1, self))

        # Carga los eventos disponibles cuando se selecciona un boton.
        self.listaBotonesTab1.itemSelectionChanged.connect(lambda: self.ModelBAP.cargarEventosConfig(self.listaBotonesTab1, self.listaEventosTab1, self))
        self.listaEventosTab1.itemSelectionChanged.connect(lambda: self.ModelBAP.cargarEventoConfig(self.listaBotonesTab1, self.listaEventosTab1, self))

        # OutsNum
        self.spinBoxOutsNumTab1.editingFinished.connect(lambda: self.ModelBAP.setOutsNumConfig(self.spinBoxOutsNumTab1))
        self.spinBoxOutsNumTab1.valueChanged.connect(lambda: self.ModelBAP.setOutsNumConfig(self.spinBoxOutsNumTab1))

        # TAB 2
        self.createConfigBAPGroupBox()
        self.createPlacasBAPGroupBox()

        self.agregarBAP2.clicked.connect(lambda: self.ModelBAP.agregarDisp(self.listWidgetPlacasBAP2, self.ConfigBAPGroupBox, labelsBAP))
        self.removerBAP2.clicked.connect(lambda: self.ModelBAP.removerDisp(self.listWidgetPlacasBAP2, self.ConfigBAPGroupBox, self.removerBAP2))

        self.guardarBAP2.clicked.connect(lambda: self.ModelBAP.guardarCambios())

        # Configuracion para BAPInfoManager.dat
        self.lineEdit1BAP.editingFinished.connect(lambda: self.ModelBAP.writeDat(self.listWidgetPlacasBAP2, self.lineEdit1BAP, 1))
        self.lineEdit2BAP.editingFinished.connect(lambda: self.ModelBAP.writeDat(self.listWidgetPlacasBAP2, self.lineEdit2BAP, 2))
        self.lineEdit3BAP.editingFinished.connect(lambda: self.ModelBAP.writeDat(self.listWidgetPlacasBAP2, self.lineEdit3BAP, 3))
        self.lineEdit4BAP.editingFinished.connect(lambda: self.ModelBAP.writeDat(self.listWidgetPlacasBAP2, self.lineEdit4BAP, 4))
        self.lineEdit5BAP.editingFinished.connect(lambda: self.ModelBAP.writeDat(self.listWidgetPlacasBAP2, self.lineEdit5BAP, 5))
        self.lineEdit6BAP.editingFinished.connect(lambda: self.ModelBAP.writeDat(self.listWidgetPlacasBAP2, self.lineEdit6BAP, 6))
        self.lineEdit7BAP.editingFinished.connect(lambda: self.ModelBAP.writeDat(self.listWidgetPlacasBAP2, self.lineEdit7BAP, 7))

        self.checkBoxBAP.stateChanged.connect(lambda: self.ModelBAP.habilitar(self.listWidgetPlacasBAP2,
                                                                              self.checkBoxBAP,
                                                                              self.lineEdit1BAP,
                                                                              self.lineEdit2BAP,
                                                                              self.lineEdit3BAP,
                                                                              self.lineEdit4BAP,
                                                                              self.lineEdit5BAP,
                                                                              self.lineEdit6BAP,
                                                                              self.lineEdit7BAP))

        # Cuando se selecciona una placa (mouse o tecla) (BAP2)
        self.listWidgetPlacasBAP2.itemSelectionChanged.connect(lambda: self.ModelBAP.cargarItem(
                                                                                            self.listWidgetPlacasBAP2,
                                                                                            self.checkBoxBAP,
                                                                                            self.removerBAP2,
                                                                                            self.lineEdit1BAP,
                                                                                            self.lineEdit2BAP,
                                                                                            self.lineEdit3BAP,
                                                                                            self.lineEdit4BAP,
                                                                                            self.lineEdit5BAP,
                                                                                            self.lineEdit6BAP,
                                                                                            self.lineEdit7BAP))

        # TAB 3
        self.createPlacasBAP3GroupBox()
        self.createConfigBAP3GroupBox()

        self.agregarBAP3.clicked.connect(lambda: self.ModelBAP.agregarDisp(self.listWidgetPlacasBAP3, self.ConfigBAP3GroupBox, labelsBAP3, 'BAP3', self))
        self.removerBAP3.clicked.connect(lambda: self.ModelBAP.removerDisp(self.listWidgetPlacasBAP3, self.ConfigBAP3GroupBox, self.removerBAP3, 'BAP3'))

        self.guardarBAP3.clicked.connect(lambda: self.ModelBAP.guardarCambios())

        # Configuracion para BAPInfoManager.dat
        self.lineEdit1BAP3.editingFinished.connect(lambda: self.ModelBAP.writeDat(self.listWidgetPlacasBAP3, self.lineEdit1BAP3, 1, 'BAP3'))
        self.lineEdit2BAP3.editingFinished.connect(lambda: self.ModelBAP.writeDat(self.listWidgetPlacasBAP3, self.lineEdit2BAP3, 2, 'BAP3'))
        self.lineEdit3BAP3.editingFinished.connect(lambda: self.ModelBAP.writeDat(self.listWidgetPlacasBAP3, self.lineEdit3BAP3, 3, 'BAP3'))
        self.lineEdit4BAP3.editingFinished.connect(lambda: self.ModelBAP.writeDat(self.listWidgetPlacasBAP3, self.lineEdit4BAP3, 4, 'BAP3'))
        self.lineEdit5BAP3.editingFinished.connect(lambda: self.ModelBAP.writeDat(self.listWidgetPlacasBAP3, self.lineEdit5BAP3, 5, 'BAP3'))
        self.lineEdit6BAP3.editingFinished.connect(lambda: self.ModelBAP.writeDat(self.listWidgetPlacasBAP3, self.lineEdit6BAP3, 6, 'BAP3'))
        self.lineEdit7BAP3.editingFinished.connect(lambda: self.ModelBAP.writeDat(self.listWidgetPlacasBAP3, self.lineEdit7BAP3, 7, 'BAP3'))

        self.checkBoxBAP3.stateChanged.connect(lambda: self.ModelBAP.habilitar(self.listWidgetPlacasBAP3, self.checkBoxBAP3, self.lineEdit1BAP3, self.lineEdit2BAP3, self.lineEdit3BAP3, self.lineEdit4BAP3, self.lineEdit5BAP3, self.lineEdit6BAP3, self.lineEdit7BAP3, 'BAP3'))

        # Cuando se modifica el spinbox OutsNum
        self.spinBoxOutsNumBAP3.editingFinished.connect(lambda: self.ModelBAP.setOutsNumPlacas(self.listWidgetPlacasBAP3, self.spinBoxOutsNumBAP3))
        self.spinBoxOutsNumBAP3.valueChanged.connect(lambda: self.ModelBAP.setOutsNumPlacas(self.listWidgetPlacasBAP3, self.spinBoxOutsNumBAP3))

        # Cada vez que se selecciona una placa BAP3 de la lista.
        self.listWidgetPlacasBAP3.itemSelectionChanged.connect(lambda: self.ModelBAP.cargarItem(
                                                                                            self.listWidgetPlacasBAP3,
                                                                                            self.checkBoxBAP3,
                                                                                            self.removerBAP3,
                                                                                            self.lineEdit1BAP3,
                                                                                            self.lineEdit2BAP3,
                                                                                            self.lineEdit3BAP3,
                                                                                            self.lineEdit4BAP3,
                                                                                            self.lineEdit5BAP3,
                                                                                            self.lineEdit6BAP3,
                                                                                            self.lineEdit7BAP3,
                                                                                            self.spinBoxOutsNumBAP3,
                                                                                            'BAP3'))

        # TAB 4
        self.createTab4GroupBox()

        # Actualiza los cambios hechos en el tab1 en el tab4
        self.tabs.currentChanged.connect(lambda: self.ModelBAP.updateTab(self.tabs, self.listaBAP3Tab4, self.listaBotonesTab4, self.listaEventosTab4, self))

        self.agregarBotonTab4.clicked.connect(lambda: self.ModelBAP.agregarBoton(self.listaBAP3Tab4, self.listaBotonesTab4, self.listaEventosTab4, self))
        self.agregarEventoTab4.clicked.connect(lambda: self.ModelBAP.agregarEvento(self.listaBAP3Tab4, self.listaBotonesTab4, self.listaEventosTab4, self))
        self.removerEventoTab4.clicked.connect(lambda: self.ModelBAP.removerEvento(self.listaBAP3Tab4, self.listaBotonesTab4, self.listaEventosTab4, self))
        self.removerBotonTab4.clicked.connect(lambda: self.ModelBAP.removerBoton(self.listaBAP3Tab4, self.listaBotonesTab4, self))

        self.guardarTab4.clicked.connect(lambda: self.ModelBAP.guardarCambios())

        # Cada vez que se selecciona una BAP3 de la lista.
        self.listaBAP3Tab4.itemSelectionChanged.connect(lambda: self.ModelBAP.cargarBotones(self.listaBAP3Tab4, self.listaBotonesTab4, self.listaEventosTab4, self))
        # Lista Botones
        self.listaBotonesTab4.itemSelectionChanged.connect(lambda: self.ModelBAP.cargarEventos(self.listaBAP3Tab4, self.listaBotonesTab4, self.listaEventosTab4, self))
        # Lista Eventos
        self.listaEventosTab4.itemSelectionChanged.connect(lambda: self.ModelBAP.cargarEvento(self.listaBAP3Tab4, self.listaBotonesTab4, self.listaEventosTab4, self))
        # Cuando se hace doble click en un boton
        self.listaBotonesTab4.itemChanged.connect(lambda: self.ModelBAP.setIdBotones(self.listaBAP3Tab4, self.listaBotonesTab4))

        # Edita Accion
        self.comboBox1Tab4.activated.connect(lambda: self.ModelBAP.setEvento(self.listaBAP3Tab4, self.listaBotonesTab4, self.listaEventosTab4, self))
        # Edita Salida
        self.spinBox1Tab4.editingFinished.connect(lambda: self.ModelBAP.setEvento(self.listaBAP3Tab4,self.listaBotonesTab4, self.listaEventosTab4, self))
        # Edita Tiempo
        self.spinBox2Tab4.editingFinished.connect(lambda: self.ModelBAP.setEvento(self.listaBAP3Tab4, self.listaBotonesTab4, self.listaEventosTab4, self))
        # Edita RespuestaOK
        self.comboBox2Tab4.activated.connect(lambda: self.ModelBAP.setEvento(self.listaBAP3Tab4, self.listaBotonesTab4, self.listaEventosTab4, self))

        # TAB 5
        self.createConfigCONGroupBox()
        self.createConsolasGroupBox()

        self.agregarCON.clicked.connect(lambda: self.ModelCON.agregarDisp(self.listWidgetConsolas, self.ConfigCONGroupBox, labelsCON))
        self.removerCON.clicked.connect(lambda: self.ModelCON.removerDisp(self.listWidgetConsolas, self.ConfigCONGroupBox, self.removerCON))

        self.guardarCON.clicked.connect(lambda: self.ModelCON.guardarCambios())

        # Configuracion para ConsoleInfoManager.dat
        self.lineEdit1CON.editingFinished.connect(lambda: self.ModelCON.writeDat(self.listWidgetConsolas, self.lineEdit1CON, 1))
        self.lineEdit2CON.editingFinished.connect(lambda: self.ModelCON.writeDat(self.listWidgetConsolas, self.lineEdit2CON, 2))
        self.lineEdit3CON.editingFinished.connect(lambda: self.ModelCON.writeDat(self.listWidgetConsolas, self.lineEdit3CON, 3))
        self.lineEdit4CON.editingFinished.connect(lambda: self.ModelCON.writeDat(self.listWidgetConsolas, self.lineEdit4CON, 4))
        self.lineEdit5CON.editingFinished.connect(lambda: self.ModelCON.writeDat(self.listWidgetConsolas, self.lineEdit5CON, 5))

        self.checkBoxCON.stateChanged.connect(lambda: self.ModelCON.habilitar(self.listWidgetConsolas,
                                                                              self.checkBoxCON,
                                                                              self.lineEdit1CON,
                                                                              self.lineEdit2CON,
                                                                              self.lineEdit3CON,
                                                                              self.lineEdit4CON,
                                                                              self.lineEdit5CON,
                                                                              self.lineEdit6CON,
                                                                              self.lineEdit7CON))

        self.listWidgetConsolas.itemSelectionChanged.connect(lambda: self.ModelCON.cargarItem(self.listWidgetConsolas,
                                                                                              self.checkBoxCON,
                                                                                              self.removerCON,
                                                                                              self.lineEdit1CON,
                                                                                              self.lineEdit2CON,
                                                                                              self.lineEdit3CON,
                                                                                              self.lineEdit4CON,
                                                                                              self.lineEdit5CON,
                                                                                              self.lineEdit6CON,
                                                                                              self.lineEdit7CON))

        # TAB 6
        self.createConfigKANGroupBox()
        self.createKantsGroupBox()

        self.agregarKAN.clicked.connect(lambda: self.ModelKAN.agregarDisp(self.listWidgetKants, self.ConfigKANGroupBox, labelsKAN))
        self.removerKAN.clicked.connect(lambda: self.ModelKAN.removerDisp(self.listWidgetKants, self.ConfigKANGroupBox, self.removerKAN))

        self.guardarKANButton.clicked.connect(lambda: self.ModelKAN.guardarCambios())

        # Configuracion para KantInfoManager.dat
        self.lineEdit1KAN.editingFinished.connect(lambda: self.ModelKAN.writeDat(self.listWidgetKants, self.lineEdit1KAN, 1))
        self.lineEdit2KAN.editingFinished.connect(lambda: self.ModelKAN.writeDat(self.listWidgetKants, self.lineEdit2KAN, 2))
        self.lineEdit3KAN.editingFinished.connect(lambda: self.ModelKAN.writeDat(self.listWidgetKants, self.lineEdit3KAN, 3))
        self.lineEdit4KAN.editingFinished.connect(lambda: self.ModelKAN.writeDat(self.listWidgetKants, self.lineEdit4KAN, 4))
        self.lineEdit5KAN.editingFinished.connect(lambda: self.ModelKAN.writeDat(self.listWidgetKants, self.lineEdit5KAN, 5))

        self.checkBoxKAN.stateChanged.connect(lambda: self.ModelKAN.habilitar(self.listWidgetKants,
                                                                              self.checkBoxKAN,
                                                                              self.lineEdit1KAN,
                                                                              self.lineEdit2KAN,
                                                                              self.lineEdit3KAN,
                                                                              self.lineEdit4KAN,
                                                                              self.lineEdit5KAN,
                                                                              self.lineEdit6KAN,
                                                                              self.lineEdit7KAN))

        self.listWidgetKants.itemSelectionChanged.connect(lambda: self.ModelKAN.cargarItem(self.listWidgetKants,
                                                                                           self.checkBoxKAN,
                                                                                           self.removerKAN,
                                                                                           self.lineEdit1KAN,
                                                                                           self.lineEdit2KAN,
                                                                                           self.lineEdit3KAN,
                                                                                           self.lineEdit4KAN,
                                                                                           self.lineEdit5KAN,
                                                                                           self.lineEdit6KAN,
                                                                                           self.lineEdit7KAN))

        # TAB 7 Configuracion Consola/Kant
        self.createConfigConsolaGroupBox()
        self.createConfigKantCommGroupBox()
        self.createConfigKeepAliveGroupBox()

        # self.guardarSP1Button.clicked.connect(lambda: self.ModelSP1.guardarCambios())     # AGREGAR BOTON SP1!!!!

        # Modificaciones del archivo Spools_PRManager.config (tab 7)
        # Configuracion Consola: Direccion Consola (IP:Port)
        self.lineEdit1Consola.editingFinished.connect(lambda: self.ModelSP1.writeConfig(self, self.lineEdit1Consola, 'PROperListener', 'LogFile', atributo='ConsoleAddress'))

        # Configuracion Consola: TCPServerListener (IP:Port)
        self.lineEdit2Consola.editingFinished.connect(lambda: self.ModelSP1.writeConfig(self, self.lineEdit2Consola, 'PROperListener', 'TCPServerListener', atributo='Address'))

        # Configuracion Consola: UDPServerListener (IP:Port)
        self.lineEdit3Consola.editingFinished.connect(lambda: self.ModelSP1.writeConfig(self, self.lineEdit3Consola, 'PRBAPListener', 'UDPServerListener', atributo='Address'))

        # Configuracion KantCommModule: Numero de nodo local
        self.lineEditNodoKant.editingFinished.connect(lambda: self.ModelSP1.writeConfig(self, self.lineEditNodoKant, 'KantCommMoule', 'PRManager', atributo='NroNodoLocal'))

        # Configuracion KantCommModule: UDPServerListener (IP:Port)
        self.lineEditUDPKant.editingFinished.connect(lambda: self.ModelSP1.writeConfig(self, self.lineEditUDPKant, 'KantCommModule', 'UDPServerListener', atributo='Address'))

        # BAPKeepAlive tab 7
        # Segs. para prevencion
        self.spinBoxSegsBAPAlive.editingFinished.connect(lambda: self.ModelSP1.writeConfig(self, self.spinBoxSegsBAPAlive, 'BAPKeepAlive', 'BAPAliveConfig', 'SecondsToPrevention'))
        self.spinBoxSegsBAPAlive.valueChanged.connect(lambda: self.ModelSP1.writeConfig(self, self.spinBoxSegsBAPAlive, 'BAPKeepAlive', 'BAPAliveConfig', 'SecondsToPrevention'))

        # Num. alives para normalizacion
        self.spinBoxNumBAPAlive.editingFinished.connect(lambda: self.ModelSP1.writeConfig(self, self.spinBoxNumBAPAlive, 'BAPKeepAlive', 'BAPAliveConfig', 'NumAlivesToNormalize'))
        self.spinBoxNumBAPAlive.valueChanged.connect(lambda: self.ModelSP1.writeConfig(self, self.spinBoxNumBAPAlive, 'BAPKeepAlive', 'BAPAliveConfig', 'NumAlivesToNormalize'))

        # Check interval
        self.spinBoxCheckBAPConfig.editingFinished.connect(lambda: self.ModelSP1.writeConfig(self, self.spinBoxCheckBAPConfig, 'BAPKeepAlive', 'CheckInterval', atributo='value'))
        self.spinBoxCheckBAPConfig.valueChanged.connect(lambda: self.ModelSP1.writeConfig(self, self.spinBoxCheckBAPConfig, 'BAPKeepAlive', 'CheckInterval', atributo='value'))

        # Default test time
        self.spinBoxDefaultBAPConfig.editingFinished.connect(lambda: self.ModelSP1.writeConfig(self, self.spinBoxDefaultBAPConfig, 'BAPKeepAlive', 'BAPConfig', 'DefaultTestTime'))
        self.spinBoxDefaultBAPConfig.valueChanged.connect(lambda: self.ModelSP1.writeConfig(self, self.spinBoxDefaultBAPConfig, 'BAPKeepAlive', 'BAPConfig', 'DefaultTestTime'))

        # SendStatusIO
        self.comboBoxStatusBAPAlive.activated.connect(lambda: self.ModelSP1.writeConfig(self, self.comboBoxStatusBAPAlive, 'BAPKeepAlive', 'BAPAliveConfig', 'SendStatusIO'))
        self.comboBoxAutoBAPAlive.activated.connect(lambda: self.ModelSP1.writeConfig(self, self.comboBoxAutoBAPAlive, 'BAPKeepAlive', 'BAPConfig', 'AutoUpdateParams'))

        # Checkbox que permite cargar datos de Configuration o de cada BAP3
        # self.checkBoxPlacas.stateChanged.connect(lambda: self.ModelBAP.configToBAP(self))

        # Carga inicial
        self.ModelSP1.loadConfig(self)     # Se pasa como argumento self de MainWindow
        self.ModelBAP.loadDat(self.listWidgetPlacasBAP2, self.ConfigBAPGroupBox, self.removerBAP2)     # BAP2
        self.ModelBAP.loadDat(self.listWidgetPlacasBAP3, self.ConfigBAP3GroupBox, self.removerBAP3, 'BAP3')  # BAP3
        self.ModelBAP.loadDat(self.listaBAP3Tab4, None, None, 'BAP3', self)    # BAP3 tab 4
        self.ModelBAP.loadConfiguration(self.listaTabs, self.listaBotonesTab1, self.listaEventosTab1, self)  # Configuration tab 1
        self.ModelCON.loadDat(self.listWidgetConsolas, self.ConfigCONGroupBox, self.removerCON)
        self.ModelKAN.loadDat(self.listWidgetKants, self.ConfigKANGroupBox, self.removerKAN)

        # Cuando se cargan los datos al inicializar se activan las funciones "stateChanged" y "valueChanged" que
        # modifican esta variable y aca se resetean.
        self.ModelSP1.modificado = False
        self.ModelBAP.modificado = False
        self.ModelCON.modificado = False
        self.ModelKAN.modificado = False

    # Cuando se cierra la ventana
    def closeEvent(self, event):
        mensaje = QMessageBox()
        mensaje.setText('¿Desea guardar los cambios efectuados antes de salir?')
        mensaje.setWindowTitle('Cerrar PRConfig')
        guardarButton = mensaje.addButton('Guardar', mensaje.YesRole)
        noguardarButton = mensaje.addButton('No guardar', mensaje.NoRole)
        cancelarButton = mensaje.addButton('Cancelar', mensaje.RejectRole)

        # Se realizo algun cambio
        if (self.ModelSP1.modificado or self.ModelBAP.modificado or self.ModelCON.modificado or self.ModelKAN.modificado) is True:
            mensaje.exec_()

            if mensaje.clickedButton() == guardarButton:
                self.ModelSP1.guardarCambios()
                self.ModelBAP.guardarCambios()
                self.ModelCON.guardarCambios()
                self.ModelKAN.guardarCambios()
                event.accept()
            elif mensaje.clickedButton() == noguardarButton:
                self.ModelSP1.borrarBackup(self.carpeta)    # Se puede usar cualquiera de los objetos.
                event.accept()
            elif mensaje.clickedButton() == cancelarButton:
                event.ignore()
        else:
            self.ModelSP1.borrarBackup(self.carpeta)    # Se puede usar cualquiera de los objetos.


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
