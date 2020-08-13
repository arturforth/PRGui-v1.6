from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QPushButton, QFileDialog


# Clase que representa la interfaz grafica dentro del esquema Model-View-Controller
class Ui_MainWindow:
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle('PRManagerConfig')
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(500, 300)
        MainWindow.setWindowIcon(QtGui.QIcon('icon.ico'))

        self.newfont = QtGui.QFont('MS Shell Dlg', 12)

        self.tabs = QtWidgets.QTabWidget(MainWindow)
        self.tabs.setGeometry(QtCore.QRect(1, 0, 500, 300))

        self.tab1 = QtWidgets.QWidget(self.tabs)
        self.tab2 = QtWidgets.QWidget(self.tabs)
        self.tab3 = QtWidgets.QWidget(self.tabs)
        self.tab4 = QtWidgets.QWidget(self.tabs)
        self.tab5 = QtWidgets.QWidget(self.tabs)
        self.tab6 = QtWidgets.QWidget(self.tabs)
        self.tab7 = QtWidgets.QWidget(self.tabs)

        self.tabs.addTab(self.tab1, "BAPInfoManager")
        self.tabs.addTab(self.tab2, "Placas BAP2")
        self.tabs.addTab(self.tab3, "Placas BAP3")
        self.tabs.addTab(self.tab4, "Configuración Placas BAP3")
        self.tabs.addTab(self.tab5, "Consolas")
        self.tabs.addTab(self.tab6, "Kants")
        self.tabs.addTab(self.tab7, "Configuración Consola/Kant")

    # Tab 1 BAPInfoManager / Configuracion
    def createConfigurationBAP3GroupBox(self):
        self.ConfigurationBAP3GroupBox = QtWidgets.QGroupBox(self.tab1)
        self.ConfigurationBAP3GroupBox.setGeometry(QtCore.QRect(15, 10, 460, 260))  # coord. x, coord. y, ancho, alto.
        self.ConfigurationBAP3GroupBox.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.ConfigurationBAP3GroupBox.setObjectName('ConfigurationBAP3GroupBox')

        self.agregarBotonTab1 = QtWidgets.QPushButton(self.ConfigurationBAP3GroupBox)
        self.agregarBotonTab1.setGeometry(QtCore.QRect(20, 30, 40, 30))
        self.agregarBotonTab1.setObjectName('agregarBotonTab1')
        self.agregarBotonTab1.setFont(self.newfont)
        # self.iconoBotonConfig = QtGui.QIcon('resources/Sirena.png')
        # self.agregarBotonTab1.setIcon(self.iconoBotonConfig)
        
        self.removerBotonTab1 = QtWidgets.QPushButton(self.ConfigurationBAP3GroupBox)
        self.removerBotonTab1.setGeometry(QtCore.QRect(155, 30, 40, 30))
        self.removerBotonTab1.setObjectName('removerBotonTab1')
        self.removerBotonTab1.setFont(self.newfont)

        self.agregarEventoTab1 = QtWidgets.QPushButton(self.ConfigurationBAP3GroupBox)
        self.agregarEventoTab1.setGeometry(QtCore.QRect(65, 30, 40, 30))
        self.agregarEventoTab1.setObjectName('agregarEventoTab1')
        self.agregarEventoTab1.setFont(self.newfont)

        self.removerEventoTab1 = QtWidgets.QPushButton(self.ConfigurationBAP3GroupBox)
        self.removerEventoTab1.setGeometry(QtCore.QRect(110, 30, 40, 30))
        self.removerEventoTab1.setObjectName('removerEventoTab1')
        self.removerEventoTab1.setFont(self.newfont)

        self.guardarTab1 = QtWidgets.QPushButton(self.ConfigurationBAP3GroupBox)
        self.guardarTab1.setGeometry(QtCore.QRect(200, 30, 40, 30))
        self.guardarTab1.setObjectName('guardarTab1')
        self.guardarTab1.setFont(self.newfont)

        # OutsNum
        self.labelspinBoxOutsNumTab1 = QtWidgets.QLabel(self.ConfigurationBAP3GroupBox)
        self.labelspinBoxOutsNumTab1.setGeometry(QtCore.QRect(335, 35, 150, 20))
        self.labelspinBoxOutsNumTab1.setText('OutsNum')

        self.spinBoxOutsNumTab1 = QtWidgets.QSpinBox(self.ConfigurationBAP3GroupBox)
        self.spinBoxOutsNumTab1.setGeometry(QtCore.QRect(395, 35, 40, 20))
        self.spinBoxOutsNumTab1.setObjectName("spinBoxOutsNumTab1")

        self.listaTabs = QtWidgets.QListWidget(self.ConfigurationBAP3GroupBox)
        self.listaTabs.setGeometry(QtCore.QRect(20, 70, 100, 170))
        self.listaTabs.setObjectName('ListaTabs')

        self.listaBotonesTab1 = QtWidgets.QListWidget(self.ConfigurationBAP3GroupBox)
        self.listaBotonesTab1.setGeometry(QtCore.QRect(130, 70, 100, 170))
        self.listaBotonesTab1.setObjectName('listaBotonesTab1')

        self.listaEventosTab1 = QtWidgets.QListWidget(self.ConfigurationBAP3GroupBox)
        self.listaEventosTab1.setGeometry(QtCore.QRect(240, 70, 100, 170))
        self.listaEventosTab1.setObjectName('listaEventosTab1')

        # Accion
        self.labelAccionTab1 = QtWidgets.QLabel(self.ConfigurationBAP3GroupBox)
        self.labelAccionTab1.setGeometry(QtCore.QRect(350, 70, 89, 16))
        self.labelAccionTab1.setObjectName("labelAccionTab1")

        self.comboBox1Tab1 = QtWidgets.QComboBox(self.ConfigurationBAP3GroupBox)
        self.comboBox1Tab1.setGeometry(QtCore.QRect(350, 90, 85, 20))
        self.comboBox1Tab1.setEditable(False)
        self.comboBox1Tab1.setObjectName("ComboAccionConfig")
        self.comboBox1Tab1.addItem("")
        self.comboBox1Tab1.addItem("")
        self.comboBox1Tab1.addItem("")

        self.comboBox1Tab1.setCurrentText("")
        self.comboBox1Tab1.setItemText(0, "PULSAR")
        self.comboBox1Tab1.setItemText(1, "ENCENDER")
        self.comboBox1Tab1.setItemText(2, "APAGAR")

        # Salida
        self.labelSalidaTab1 = QtWidgets.QLabel(self.ConfigurationBAP3GroupBox)
        self.labelSalidaTab1.setGeometry(QtCore.QRect(350, 110, 89, 16))
        self.labelSalidaTab1.setObjectName("labelSalidaTab1")

        self.spinBox1Tab1 = QtWidgets.QSpinBox(self.ConfigurationBAP3GroupBox)
        self.spinBox1Tab1.setGeometry(QtCore.QRect(350, 130, 85, 20))
        self.spinBox1Tab1.setObjectName("spinBox1Tab1")

        # Tiempo
        self.labelTiempoTab1 = QtWidgets.QLabel(self.ConfigurationBAP3GroupBox)
        self.labelTiempoTab1.setGeometry(QtCore.QRect(350, 150, 89, 16))
        self.labelTiempoTab1.setObjectName("labelTiempoTab1")

        self.spinBox2Tab1 = QtWidgets.QSpinBox(self.ConfigurationBAP3GroupBox)
        self.spinBox2Tab1.setGeometry(QtCore.QRect(350, 170, 85, 20))
        self.spinBox2Tab1.setObjectName("spinBox2Tab1")

        # Respuesta OK
        self.labelRtaOKTab1 = QtWidgets.QLabel(self.ConfigurationBAP3GroupBox)
        self.labelRtaOKTab1.setGeometry(QtCore.QRect(350, 190, 89, 16))
        self.labelRtaOKTab1.setObjectName("labelRtaOKTab1")

        self.comboBox2Tab1 = QtWidgets.QComboBox(self.ConfigurationBAP3GroupBox)
        self.comboBox2Tab1.setGeometry(QtCore.QRect(350, 210, 85, 20))
        self.comboBox2Tab1.setEditable(False)
        self.comboBox2Tab1.setObjectName("RtaOKConfigGroupBox")
        self.comboBox2Tab1.addItem("")
        self.comboBox2Tab1.addItem("")
        self.comboBox2Tab1.addItem("")

        self.comboBox2Tab1.setCurrentText("")
        self.comboBox2Tab1.setItemText(0, "PULSADA")
        self.comboBox2Tab1.setItemText(1, "ENCENDIDA")
        self.comboBox2Tab1.setItemText(2, "APAGADA")

        self.agregarBotonTab1.setText('+B')
        self.agregarEventoTab1.setText('+E')
        self.removerEventoTab1.setText('E')
        self.removerBotonTab1.setText('B')
        self.guardarTab1.setText('')

        self.labelAccionTab1.setText('Accion')
        self.labelSalidaTab1.setText('Salida')
        self.labelTiempoTab1.setText('Tiempo')
        self.labelRtaOKTab1.setText('Respuesta OK')

        # Textos
        self.ConfigurationBAP3GroupBox.setTitle('Configuracion BapInfoManager')

    # Tab 2 BAPInfoManager / Placas BAP2
    # TODO: Cambiar todos los nombres a BAP2
    def createPlacasBAPGroupBox(self):
        self.PlacasGroupBox = QtWidgets.QGroupBox(self.tab2)
        self.PlacasGroupBox.setGeometry(QtCore.QRect(15, 10, 180, 260))  # coord. x, coord. y, ancho, alto.
        self.PlacasGroupBox.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.PlacasGroupBox.setObjectName('PlacasGroupBox')

        self.agregarBAP2 = QtWidgets.QPushButton(self.PlacasGroupBox)
        self.agregarBAP2.setGeometry(QtCore.QRect(20, 30, 42, 30))
        self.agregarBAP2.setObjectName('AgregarBAP2')
        self.agregarBAP2.setFont(self.newfont)

        self.removerBAP2 = QtWidgets.QPushButton(self.PlacasGroupBox)
        self.removerBAP2.setGeometry(QtCore.QRect(69, 30, 42, 30))
        self.removerBAP2.setObjectName('RemoverBAP2')
        self.removerBAP2.setFont(self.newfont)

        self.guardarBAP2 = QtWidgets.QPushButton(self.PlacasGroupBox)
        self.guardarBAP2.setGeometry(QtCore.QRect(118, 30, 42, 30))
        self.guardarBAP2.setObjectName('GuardarBAP22')
        self.guardarBAP2.setFont(self.newfont)

        self.listWidgetPlacasBAP2 = QtWidgets.QListWidget(self.PlacasGroupBox)
        self.listWidgetPlacasBAP2.setGeometry(QtCore.QRect(20, 70, 140, 170))
        self.listWidgetPlacasBAP2.setObjectName('listWidgetPlacasBAP2')

        self.PlacasGroupBox.setTitle('Placas BAP2 existentes')

        self.agregarBAP2.setText('+')
        self.removerBAP2.setText('')
        self.guardarBAP2.setText('')

        self.agregarBAP2.setToolTip('Agregar placa BAP')
        self.removerBAP2.setToolTip('Eliminar placa BAP seleccionada')
        self.guardarBAP2.setToolTip('Guardar cambios')

    def createConfigBAPGroupBox(self):
        self.ConfigBAPGroupBox = QtWidgets.QGroupBox(self.tab2)
        self.ConfigBAPGroupBox.setGeometry(QtCore.QRect(210, 10, 180, 260))
        self.ConfigBAPGroupBox.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.ConfigBAPGroupBox.setObjectName('ConfigBAPGroupBox')

        self.checkBoxBAP = QtWidgets.QCheckBox(self.ConfigBAPGroupBox)
        self.checkBoxBAP.setObjectName('checkBox')
        self.checkBoxBAP.setGeometry(QtCore.QRect(15, 30, 150, 20))

        self.lineEdit1BAP = QtWidgets.QLineEdit(self.ConfigBAPGroupBox)
        self.lineEdit1BAP.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit1BAP.setObjectName('lineEdit1BAP')
        self.lineEdit1BAP.setGeometry(QtCore.QRect(15, 70, 150, 20))

        self.lineEdit2BAP = QtWidgets.QLineEdit(self.ConfigBAPGroupBox)
        self.lineEdit2BAP.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit2BAP.setObjectName('lineEdit2BAP')
        self.lineEdit2BAP.setGeometry(QtCore.QRect(15, 95, 150, 20))

        self.lineEdit3BAP = QtWidgets.QLineEdit(self.ConfigBAPGroupBox)
        self.lineEdit3BAP.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit3BAP.setObjectName('lineEdit3BAP')
        self.lineEdit3BAP.setGeometry(QtCore.QRect(15, 120, 150, 20))

        self.lineEdit4BAP = QtWidgets.QLineEdit(self.ConfigBAPGroupBox)
        self.lineEdit4BAP.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit4BAP.setObjectName('lineEdit4BAP')
        self.lineEdit4BAP.setGeometry(QtCore.QRect(15, 145, 150, 20))

        self.lineEdit5BAP = QtWidgets.QLineEdit(self.ConfigBAPGroupBox)
        self.lineEdit5BAP.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit5BAP.setObjectName('lineEdit5BAP')
        self.lineEdit5BAP.setGeometry(QtCore.QRect(15, 170, 150, 20))

        self.lineEdit6BAP = QtWidgets.QLineEdit(self.ConfigBAPGroupBox)
        self.lineEdit6BAP.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit6BAP.setObjectName('lineEdit6BAP')
        self.lineEdit6BAP.setGeometry(QtCore.QRect(15, 195, 150, 20))

        self.lineEdit7BAP = QtWidgets.QLineEdit(self.ConfigBAPGroupBox)
        self.lineEdit7BAP.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit7BAP.setObjectName('lineEdit7BAP')
        self.lineEdit7BAP.setGeometry(QtCore.QRect(15, 220, 150, 20))

        self.ConfigBAPGroupBox.setTitle('Configuración BAP2')
        self.checkBoxBAP.setText('Habilitar BAP2')

        self.lineEdit1BAP.setPlaceholderText('Número de abonado')
        self.lineEdit2BAP.setPlaceholderText('Número de la sucursal')
        self.lineEdit3BAP.setPlaceholderText('Nombre de la sucursal')
        self.lineEdit4BAP.setPlaceholderText('Información extra')
        self.lineEdit5BAP.setPlaceholderText('Dirección IP : Puerto')
        self.lineEdit6BAP.setPlaceholderText('Número de abonado Kant')
        self.lineEdit7BAP.setPlaceholderText('Id. de la placa')

        self.lineEdit1BAP.setToolTip('Número de abonado')
        self.lineEdit2BAP.setToolTip('Número de la sucursal')
        self.lineEdit3BAP.setToolTip('Nombre de la sucursal')
        self.lineEdit4BAP.setToolTip('Información extra')
        self.lineEdit5BAP.setToolTip('Dirección IP : Puerto')
        self.lineEdit6BAP.setToolTip('Número de abonado Kant')
        self.lineEdit7BAP.setToolTip('Id. de la placa')

    # Tab 3 BAPInfoManager / Placas BAP3
    def createPlacasBAP3GroupBox(self):
        self.PlacasBAP3GroupBox = QtWidgets.QGroupBox(self.tab3)
        self.PlacasBAP3GroupBox.setGeometry(QtCore.QRect(15, 10, 180, 260))  # coord. x, coord. y, ancho, alto.
        self.PlacasBAP3GroupBox.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.PlacasBAP3GroupBox.setObjectName('PlacasBAP3GroupBox')

        self.agregarBAP3 = QtWidgets.QPushButton(self.PlacasBAP3GroupBox)
        self.agregarBAP3.setGeometry(QtCore.QRect(20, 30, 42, 30))
        self.agregarBAP3.setObjectName('AgregarBAP3')
        self.agregarBAP3.setFont(self.newfont)

        self.removerBAP3 = QtWidgets.QPushButton(self.PlacasBAP3GroupBox)
        self.removerBAP3.setGeometry(QtCore.QRect(69, 30, 42, 30))
        self.removerBAP3.setObjectName('RemoverBAP3')
        self.removerBAP3.setFont(self.newfont)

        self.guardarBAP3 = QtWidgets.QPushButton(self.PlacasBAP3GroupBox)
        self.guardarBAP3.setGeometry(QtCore.QRect(118, 30, 42, 30))
        self.guardarBAP3.setObjectName('GuardarBAP3')
        self.guardarBAP3.setFont(self.newfont)

        self.listWidgetPlacasBAP3 = QtWidgets.QListWidget(self.PlacasBAP3GroupBox)
        self.listWidgetPlacasBAP3.setGeometry(QtCore.QRect(20, 70, 140, 170))
        self.listWidgetPlacasBAP3.setObjectName('listWidgetPlacasBAP3')

        # Placas BAP3
        self.PlacasBAP3GroupBox.setTitle('Placas BAP3 existentes')

        self.agregarBAP3.setText('+')
        self.removerBAP3.setText('')
        self.guardarBAP3.setText('')

        self.agregarBAP3.setToolTip('Agregar placa BAP')
        self.removerBAP3.setToolTip('Eliminar placa BAP seleccionada')
        self.guardarBAP3.setToolTip('Guardar cambios')

    def createConfigBAP3GroupBox(self):
        self.ConfigBAP3GroupBox = QtWidgets.QGroupBox(self.tab3)
        self.ConfigBAP3GroupBox.setGeometry(QtCore.QRect(210, 10, 265, 260))
        self.ConfigBAP3GroupBox.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.ConfigBAP3GroupBox.setObjectName('ConfigBAP3GroupBox')

        self.checkBoxBAP3 = QtWidgets.QCheckBox(self.ConfigBAP3GroupBox)
        self.checkBoxBAP3.setObjectName('checkBox')
        self.checkBoxBAP3.setGeometry(QtCore.QRect(15, 30, 150, 20))

        self.lineEdit1BAP3 = QtWidgets.QLineEdit(self.ConfigBAP3GroupBox)
        self.lineEdit1BAP3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit1BAP3.setObjectName('lineEdit1BAP3')
        self.lineEdit1BAP3.setGeometry(QtCore.QRect(15, 70, 150, 20))

        self.lineEdit2BAP3 = QtWidgets.QLineEdit(self.ConfigBAP3GroupBox)
        self.lineEdit2BAP3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit2BAP3.setObjectName('lineEdit2BAP3')
        self.lineEdit2BAP3.setGeometry(QtCore.QRect(15, 95, 150, 20))

        self.lineEdit3BAP3 = QtWidgets.QLineEdit(self.ConfigBAP3GroupBox)
        self.lineEdit3BAP3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit3BAP3.setObjectName('lineEdit3BAP3')
        self.lineEdit3BAP3.setGeometry(QtCore.QRect(15, 120, 150, 20))

        self.lineEdit4BAP3 = QtWidgets.QLineEdit(self.ConfigBAP3GroupBox)
        self.lineEdit4BAP3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit4BAP3.setObjectName('lineEdit4BAP3')
        self.lineEdit4BAP3.setGeometry(QtCore.QRect(15, 145, 150, 20))

        self.lineEdit5BAP3 = QtWidgets.QLineEdit(self.ConfigBAP3GroupBox)
        self.lineEdit5BAP3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit5BAP3.setObjectName('lineEdit5BAP3')
        self.lineEdit5BAP3.setGeometry(QtCore.QRect(15, 170, 150, 20))

        self.lineEdit6BAP3 = QtWidgets.QLineEdit(self.ConfigBAP3GroupBox)
        self.lineEdit6BAP3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit6BAP3.setObjectName('lineEdit6BAP3')
        self.lineEdit6BAP3.setGeometry(QtCore.QRect(15, 195, 150, 20))

        self.lineEdit7BAP3 = QtWidgets.QLineEdit(self.ConfigBAP3GroupBox)
        self.lineEdit7BAP3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit7BAP3.setObjectName('lineEdit7BAP3')
        self.lineEdit7BAP3.setGeometry(QtCore.QRect(15, 220, 150, 20))

        # OutsNum
        self.labelspinBoxOutsNumBAP3 = QtWidgets.QLabel(self.ConfigBAP3GroupBox)
        self.labelspinBoxOutsNumBAP3.setGeometry(QtCore.QRect(140, 30, 150, 20))
        self.labelspinBoxOutsNumBAP3.setText('OutsNum')

        self.spinBoxOutsNumBAP3 = QtWidgets.QSpinBox(self.ConfigBAP3GroupBox)
        self.spinBoxOutsNumBAP3.setGeometry(QtCore.QRect(200, 30, 40, 20))
        self.spinBoxOutsNumBAP3.setObjectName("OutsNumBAP3GroupBox")

        self.ConfigBAP3GroupBox.setTitle('Configuración BAP3')
        self.checkBoxBAP3.setText('Habilitar BAP3')

        self.lineEdit1BAP3.setPlaceholderText('Número de abonado')
        self.lineEdit2BAP3.setPlaceholderText('Número de la sucursal')
        self.lineEdit3BAP3.setPlaceholderText('Nombre de la sucursal')
        self.lineEdit4BAP3.setPlaceholderText('Información extra')
        self.lineEdit5BAP3.setPlaceholderText('Dirección IP : Puerto')
        self.lineEdit6BAP3.setPlaceholderText('Número de abonado Kant')
        self.lineEdit7BAP3.setPlaceholderText('Id. de la placa')

        self.lineEdit1BAP3.setToolTip('Número de abonado')
        self.lineEdit2BAP3.setToolTip('Número de la sucursal')
        self.lineEdit3BAP3.setToolTip('Nombre de la sucursal')
        self.lineEdit4BAP3.setToolTip('Información extra')
        self.lineEdit5BAP3.setToolTip('Dirección IP : Puerto')
        self.lineEdit6BAP3.setToolTip('Número de abonado Kant')
        self.lineEdit7BAP3.setToolTip('Id. de la placa')

    # Tab 4 Configuracion Placas BAP3
    def createTab4GroupBox(self):
        self.tab4GroupBox = QtWidgets.QGroupBox(self.tab4)
        self.tab4GroupBox.setGeometry(QtCore.QRect(15, 10, 460, 260))  # coord. x, coord. y, ancho, alto.
        self.tab4GroupBox.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.tab4GroupBox.setObjectName('tab4GroupBox')

        self.tab4GroupBox.setTitle('Configuración BAP3')

        self.agregarBotonTab4 = QtWidgets.QPushButton(self.tab4GroupBox)
        self.agregarBotonTab4.setGeometry(QtCore.QRect(20, 30, 40, 30))
        self.agregarBotonTab4.setObjectName('agregarBotonTab4')
        self.agregarBotonTab4.setFont(self.newfont)

        self.agregarEventoTab4 = QtWidgets.QPushButton(self.tab4GroupBox)
        self.agregarEventoTab4.setGeometry(QtCore.QRect(65, 30, 40, 30))
        self.agregarEventoTab4.setObjectName('agregarEventoTab4')
        self.agregarEventoTab4.setFont(self.newfont)

        self.removerEventoTab4 = QtWidgets.QPushButton(self.tab4GroupBox)
        self.removerEventoTab4.setGeometry(QtCore.QRect(110, 30, 40, 30))
        self.removerEventoTab4.setObjectName('removerEventoTab4')
        self.removerEventoTab4.setFont(self.newfont)

        self.removerBotonTab4 = QtWidgets.QPushButton(self.tab4GroupBox)
        self.removerBotonTab4.setGeometry(QtCore.QRect(155, 30, 40, 30))
        self.removerBotonTab4.setObjectName('removerBotonTab4')
        self.removerBotonTab4.setFont(self.newfont)

        self.guardarTab4 = QtWidgets.QPushButton(self.tab4GroupBox)
        self.guardarTab4.setGeometry(QtCore.QRect(200, 30, 40, 30))
        self.guardarTab4.setObjectName('guardarTab4')
        self.guardarTab4.setFont(self.newfont)

        self.listaBAP3Tab4 = QtWidgets.QListWidget(self.tab4GroupBox)
        self.listaBAP3Tab4.setGeometry(QtCore.QRect(20, 70, 100, 170))
        self.listaBAP3Tab4.setObjectName('listaBAP3Tab4')

        self.listaBotonesTab4 = QtWidgets.QListWidget(self.tab4GroupBox)
        self.listaBotonesTab4.setGeometry(QtCore.QRect(130, 70, 100, 170))
        self.listaBotonesTab4.setObjectName('listaBotonesTab4')

        self.listaEventosTab4 = QtWidgets.QListWidget(self.tab4GroupBox)
        self.listaEventosTab4.setGeometry(QtCore.QRect(240, 70, 100, 170))
        self.listaEventosTab4.setObjectName('listaEventosTab4')

        # Accion
        self.labelAccionTab4 = QtWidgets.QLabel(self.tab4GroupBox)
        self.labelAccionTab4.setGeometry(QtCore.QRect(350, 70, 89, 16))
        self.labelAccionTab4.setObjectName("labelAccionTab4")

        self.labelAccionTab4.setText('Accion')

        self.comboBox1Tab4 = QtWidgets.QComboBox(self.tab4GroupBox)
        self.comboBox1Tab4.setGeometry(QtCore.QRect(350, 90, 85, 20))
        self.comboBox1Tab4.setEditable(False)
        self.comboBox1Tab4.setObjectName("AccionPlacasBAP3GroupBox")
        self.comboBox1Tab4.addItem("")
        self.comboBox1Tab4.addItem("")
        self.comboBox1Tab4.addItem("")

        self.comboBox1Tab4.setCurrentText("")
        self.comboBox1Tab4.setItemText(0, "PULSAR")
        self.comboBox1Tab4.setItemText(1, "ENCENDER")
        self.comboBox1Tab4.setItemText(2, "APAGAR")

        # Salida
        self.labelSalidaTab4 = QtWidgets.QLabel(self.tab4GroupBox)
        self.labelSalidaTab4.setGeometry(QtCore.QRect(350, 110, 89, 16))
        self.labelSalidaTab4.setObjectName("labelSalidaTab4")

        self.labelSalidaTab4.setText('Salida')

        self.spinBox1Tab4 = QtWidgets.QSpinBox(self.tab4GroupBox)
        self.spinBox1Tab4.setGeometry(QtCore.QRect(350, 130, 85, 20))
        self.spinBox1Tab4.setObjectName("spinBox1Tab4")

        # Tiempo
        self.labelTiempoTab4 = QtWidgets.QLabel(self.tab4GroupBox)
        self.labelTiempoTab4.setGeometry(QtCore.QRect(350, 150, 89, 16))
        self.labelTiempoTab4.setObjectName("labelTiempoTab4")

        self.labelTiempoTab4.setText('Tiempo')

        self.spinBox2Tab4 = QtWidgets.QSpinBox(self.tab4GroupBox)
        self.spinBox2Tab4.setGeometry(QtCore.QRect(350, 170, 85, 20))
        self.spinBox2Tab4.setObjectName("spinBox2Tab4")

        # Respuesta OK
        self.labelRtaOKTab4 = QtWidgets.QLabel(self.tab4GroupBox)
        self.labelRtaOKTab4.setGeometry(QtCore.QRect(350, 190, 89, 16))
        self.labelRtaOKTab4.setObjectName("labelRtaOKTab4")

        self.labelRtaOKTab4.setText('Respuesta OK')

        self.comboBox2Tab4 = QtWidgets.QComboBox(self.tab4GroupBox)
        self.comboBox2Tab4.setGeometry(QtCore.QRect(350, 210, 85, 20))
        self.comboBox2Tab4.setEditable(False)
        self.comboBox2Tab4.setObjectName("RtaOKtab4GroupBox")
        self.comboBox2Tab4.addItem("")
        self.comboBox2Tab4.addItem("")
        self.comboBox2Tab4.addItem("")

        self.comboBox2Tab4.setCurrentText("")
        self.comboBox2Tab4.setItemText(0, "PULSADA")
        self.comboBox2Tab4.setItemText(1, "ENCENDIDA")
        self.comboBox2Tab4.setItemText(2, "APAGADA")

        # Textos
        # Configuracion Placas BAP3 / Tab 4
        self.agregarBotonTab4.setText('+B')
        self.agregarEventoTab4.setText('+E')
        self.removerEventoTab4.setText('E')
        self.removerBotonTab4.setText('B')
        self.guardarTab4.setText('')

        self.agregarBotonTab4.setToolTip('Agregar Boton')
        self.agregarEventoTab4.setToolTip('Agrega Evento')
        self.removerEventoTab4.setToolTip('Eliminar Evento seleccionado')
        self.removerBotonTab4.setToolTip('Eliminar Boton seleccionado')
        self.guardarTab4.setToolTip('Guardar cambios')

    # Tab 5 ConsoleInfoManager / Consolas
    def createConsolasGroupBox(self):
        self.ConsolasGroupBox = QtWidgets.QGroupBox(self.tab5)
        self.ConsolasGroupBox.setGeometry(QtCore.QRect(15, 10, 180, 260))  # coord. x, coord. y, ancho, alto.
        self.ConsolasGroupBox.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.ConsolasGroupBox.setObjectName('ConsolasGroupBox')

        self.agregarCON = QtWidgets.QPushButton(self.ConsolasGroupBox)
        self.agregarCON.setGeometry(QtCore.QRect(20, 30, 42, 30))
        self.agregarCON.setObjectName('agregarCON')
        self.agregarCON.setFont(self.newfont)

        self.removerCON = QtWidgets.QPushButton(self.ConsolasGroupBox)
        self.removerCON.setGeometry(QtCore.QRect(69, 30, 42, 30))
        self.removerCON.setObjectName('RemoverCON')
        self.removerCON.setFont(self.newfont)

        self.guardarCON = QtWidgets.QPushButton(self.ConsolasGroupBox)
        self.guardarCON.setGeometry(QtCore.QRect(118, 30, 42, 30))
        self.guardarCON.setObjectName('GuardarCON')
        self.guardarCON.setFont(self.newfont)

        self.listWidgetConsolas = QtWidgets.QListWidget(self.ConsolasGroupBox)
        self.listWidgetConsolas.setGeometry(QtCore.QRect(20, 70, 140, 170))
        self.listWidgetConsolas.setObjectName('listWidgetConsolas')

        self.ConsolasGroupBox.setTitle('Consolas existentes')

        self.agregarCON.setText('+')
        self.removerCON.setText('')
        self.guardarCON.setText('')

        self.agregarCON.setToolTip('Agregar consola')
        self.removerCON.setToolTip('Eliminar consola seleccionada')
        self.guardarCON.setToolTip('Guardar cambios')

    def createConfigCONGroupBox(self):
        self.ConfigCONGroupBox = QtWidgets.QGroupBox(self.tab5)
        self.ConfigCONGroupBox.setGeometry(QtCore.QRect(210, 10, 180, 260))
        self.ConfigCONGroupBox.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.ConfigCONGroupBox.setObjectName('ConfigBAPGroupBox')

        self.checkBoxCON = QtWidgets.QCheckBox(self.ConfigCONGroupBox)
        self.checkBoxCON.setObjectName('checkBoxCON')
        self.checkBoxCON.setGeometry(QtCore.QRect(15, 30, 150, 20))

        self.lineEdit1CON = QtWidgets.QLineEdit(self.ConfigCONGroupBox)
        self.lineEdit1CON.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit1CON.setObjectName('lineEdit1CON')
        self.lineEdit1CON.setGeometry(QtCore.QRect(15, 70, 150, 20))

        self.lineEdit2CON = QtWidgets.QLineEdit(self.ConfigCONGroupBox)
        self.lineEdit2CON.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit2CON.setObjectName('lineEdit2CON')
        self.lineEdit2CON.setGeometry(QtCore.QRect(15, 95, 150, 20))

        self.lineEdit3CON = QtWidgets.QLineEdit(self.ConfigCONGroupBox)
        self.lineEdit3CON.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit3CON.setObjectName('lineEdit3CON')
        self.lineEdit3CON.setGeometry(QtCore.QRect(15, 120, 150, 20))

        self.lineEdit4CON = QtWidgets.QLineEdit(self.ConfigCONGroupBox)
        self.lineEdit4CON.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit4CON.setObjectName('lineEdit4CON')
        self.lineEdit4CON.setGeometry(QtCore.QRect(15, 145, 150, 20))

        self.lineEdit5CON = QtWidgets.QLineEdit(self.ConfigCONGroupBox)
        self.lineEdit5CON.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit5CON.setObjectName('lineEdit5CON')
        self.lineEdit5CON.setGeometry(QtCore.QRect(15, 170, 150, 20))

        # Dummies
        self.lineEdit6CON = QtWidgets.QLineEdit(self.ConfigCONGroupBox)
        self.lineEdit7CON = QtWidgets.QLineEdit(self.ConfigCONGroupBox)

        self.lineEdit6CON.setVisible(False)
        self.lineEdit7CON.setVisible(False)

        self.ConfigCONGroupBox.setTitle('Configuración consola')
        self.checkBoxCON.setText('Habilitar Consola')

        self.lineEdit1CON.setPlaceholderText('Id. consola')
        self.lineEdit2CON.setPlaceholderText('Nombre de consola')
        self.lineEdit3CON.setPlaceholderText('Información extra')
        self.lineEdit4CON.setPlaceholderText('Dirección IP')
        self.lineEdit5CON.setPlaceholderText('Número de nodo Kant')

        self.lineEdit1CON.setToolTip('Id. consola')
        self.lineEdit2CON.setToolTip('Nombre de consola')
        self.lineEdit3CON.setToolTip('Información extra')
        self.lineEdit4CON.setToolTip('Dirección IP')
        self.lineEdit5CON.setToolTip('Número de nodo Kant')

    # Tab 6 KantsInfoManager / Kants
    def createKantsGroupBox(self):
        self.KantsGroupBox = QtWidgets.QGroupBox(self.tab6)
        self.KantsGroupBox.setGeometry(QtCore.QRect(15, 10, 180, 260))  # coord. x, coord. y, ancho, alto.
        self.KantsGroupBox.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.KantsGroupBox.setObjectName('KantsGroupBox')

        self.listWidgetKants = QtWidgets.QListWidget(self.KantsGroupBox)
        self.listWidgetKants.setGeometry(QtCore.QRect(20, 70, 140, 170))
        self.listWidgetKants.setObjectName('listWidgetKants')

        self.agregarKAN = QtWidgets.QPushButton(self.KantsGroupBox)
        self.agregarKAN.setGeometry(QtCore.QRect(20, 30, 42, 30))
        self.agregarKAN.setObjectName('agregarKAN')
        self.agregarKAN.setFont(self.newfont)

        self.removerKAN = QtWidgets.QPushButton(self.KantsGroupBox)
        self.removerKAN.setGeometry(QtCore.QRect(69, 30, 42, 30))
        self.removerKAN.setObjectName('removerKAN')
        self.removerKAN.setFont(self.newfont)

        self.guardarKANButton = QtWidgets.QPushButton(self.KantsGroupBox)
        self.guardarKANButton.setGeometry(QtCore.QRect(118, 30, 42, 30))
        self.guardarKANButton.setObjectName('GuardarKANButton')
        self.guardarKANButton.setFont(self.newfont)

        self.KantsGroupBox.setTitle('Kants existentes')

        self.agregarKAN.setText('+')
        self.removerKAN.setText('')
        self.guardarKANButton.setText('')

        self.agregarKAN.setToolTip('Agregar Kant')
        self.removerKAN.setToolTip('Eliminar Kant seleccionado')
        self.guardarKANButton.setToolTip('Guardar cambios')

    def createConfigKANGroupBox(self):
        self.ConfigKANGroupBox = QtWidgets.QGroupBox(self.tab6)
        self.ConfigKANGroupBox.setGeometry(QtCore.QRect(210, 10, 180, 260))
        self.ConfigKANGroupBox.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.ConfigKANGroupBox.setObjectName('ConfigKANGroupBox')

        self.checkBoxKAN = QtWidgets.QCheckBox(self.ConfigKANGroupBox)
        self.checkBoxKAN.setObjectName('checkBoxCON')
        self.checkBoxKAN.setGeometry(QtCore.QRect(15, 30, 150, 20))

        self.lineEdit1KAN = QtWidgets.QLineEdit(self.ConfigKANGroupBox)
        self.lineEdit1KAN.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit1KAN.setObjectName('lineEdit1KAN')
        self.lineEdit1KAN.setGeometry(QtCore.QRect(15, 70, 150, 20))

        self.lineEdit2KAN = QtWidgets.QLineEdit(self.ConfigKANGroupBox)
        self.lineEdit2KAN.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit2KAN.setObjectName('lineEdit2KAN')
        self.lineEdit2KAN.setGeometry(QtCore.QRect(15, 95, 150, 20))

        self.lineEdit3KAN = QtWidgets.QLineEdit(self.ConfigKANGroupBox)
        self.lineEdit3KAN.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit3KAN.setObjectName('lineEdit3KAN')
        self.lineEdit3KAN.setGeometry(QtCore.QRect(15, 120, 150, 20))

        self.lineEdit4KAN = QtWidgets.QLineEdit(self.ConfigKANGroupBox)
        self.lineEdit4KAN.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit4KAN.setObjectName('lineEdit4KAN')
        self.lineEdit4KAN.setGeometry(QtCore.QRect(15, 145, 150, 20))

        self.lineEdit5KAN = QtWidgets.QLineEdit(self.ConfigKANGroupBox)
        self.lineEdit5KAN.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit5KAN.setObjectName('lineEdit5KAN')
        self.lineEdit5KAN.setGeometry(QtCore.QRect(15, 170, 150, 20))

        # Dummies
        self.lineEdit6KAN = QtWidgets.QLineEdit(self.ConfigKANGroupBox)
        self.lineEdit7KAN = QtWidgets.QLineEdit(self.ConfigKANGroupBox)

        self.lineEdit6KAN.setVisible(False)
        self.lineEdit7KAN.setVisible(False)

        # Textos KantsInfoManager
        self.ConfigKANGroupBox.setTitle('Configuración Kant')
        self.checkBoxKAN.setText('Habilitar Kant')

        self.lineEdit1KAN.setPlaceholderText('Número de nodo Kant')
        self.lineEdit2KAN.setPlaceholderText('Nombre Kant')
        self.lineEdit3KAN.setPlaceholderText('Dirección IP : Puerto')
        self.lineEdit4KAN.setPlaceholderText('Frecuencia de BAP alive')
        self.lineEdit5KAN.setPlaceholderText('Frecuencia de reintento')

        self.lineEdit1KAN.setToolTip('Número de nodo Kant')
        self.lineEdit2KAN.setToolTip('Nombre Kant')
        self.lineEdit3KAN.setToolTip('Direccion IP : Puerto')
        self.lineEdit4KAN.setToolTip('Frecuencia de BAP alive')
        self.lineEdit5KAN.setToolTip('Frecuencia reintento')

    # Tab 7 Configuracion Consola/Kant
    def createConfigConsolaGroupBox(self):
        self.GroupBoxConsola = QtWidgets.QGroupBox(self.tab7)
        self.GroupBoxConsola.setGeometry(QtCore.QRect(15, 10, 225, 151))
        self.GroupBoxConsola.setObjectName("GroupBoxConsola")

        self.lineEdit1Consola = QtWidgets.QLineEdit(self.GroupBoxConsola)
        self.lineEdit1Consola.setGeometry(QtCore.QRect(20, 40, 150, 20))
        self.lineEdit1Consola.setObjectName("lineEdit1Consola")

        self.lineEdit2Consola = QtWidgets.QLineEdit(self.GroupBoxConsola)
        self.lineEdit2Consola.setGeometry(QtCore.QRect(20, 80, 150, 20))
        self.lineEdit2Consola.setObjectName("lineEdit2Consola")

        self.lineEdit3Consola = QtWidgets.QLineEdit(self.GroupBoxConsola)
        self.lineEdit3Consola.setGeometry(QtCore.QRect(20, 120, 150, 20))
        self.lineEdit3Consola.setObjectName("lineEdit3Consola")

        self.label1Consola = QtWidgets.QLabel(self.GroupBoxConsola)
        self.label1Consola.setGeometry(QtCore.QRect(20, 20, 170, 16))
        self.label1Consola.setObjectName("label1Consola")

        self.label2Consola = QtWidgets.QLabel(self.GroupBoxConsola)
        self.label2Consola.setGeometry(QtCore.QRect(20, 60, 170, 16))
        self.label2Consola.setObjectName("label2Consola")

        self.label3Consola = QtWidgets.QLabel(self.GroupBoxConsola)
        self.label3Consola.setGeometry(QtCore.QRect(20, 100, 170, 16))
        self.label3Consola.setObjectName("label3Consola")

        # Configuracion Consola/Kant
        self.GroupBoxConsola.setTitle('Configuracion Consola')
        self.label1Consola.setText('Dirección Consola (IP:Port)')
        self.label2Consola.setText('TCP Server Listener (IP:Port)')
        self.label3Consola.setText('UDP Server Listener (IP:Port)')

        self.lineEdit3Consola.setToolTip('IP y puerto del servidor al que debe reportarse')

    def createConfigKantCommGroupBox(self):
        self.GroupBoxKant = QtWidgets.QGroupBox(self.tab7)
        self.GroupBoxKant.setGeometry(QtCore.QRect(250, 10, 225, 151))
        self.GroupBoxKant.setObjectName("GroupBoxKant")

        # Numero de nodo local
        self.labelNodoKant = QtWidgets.QLabel(self.GroupBoxKant)
        self.labelNodoKant.setGeometry(QtCore.QRect(20, 20, 170, 16))
        self.labelNodoKant.setObjectName("labelNodoKant")

        self.lineEditNodoKant = QtWidgets.QLineEdit(self.GroupBoxKant)
        self.lineEditNodoKant.setGeometry(QtCore.QRect(20, 40, 151, 20))
        self.lineEditNodoKant.setObjectName("lineEditNodoKant")

        # UDP Server Address
        self.labelUDPKant = QtWidgets.QLabel(self.GroupBoxKant)
        self.labelUDPKant.setGeometry(QtCore.QRect(20, 60, 170, 16))
        self.labelUDPKant.setObjectName("labelUDPKant")

        self.lineEditUDPKant = QtWidgets.QLineEdit(self.GroupBoxKant)
        self.lineEditUDPKant.setGeometry(QtCore.QRect(20, 80, 151, 20))
        self.lineEditUDPKant.setObjectName("lineEditUDPKant")

        # Textos Configuracion KantCommModule
        self.GroupBoxKant.setTitle('Configuracion KantCommModule')
        self.labelUDPKant.setText('UDP Server Address (IP:Port)')
        self.labelNodoKant.setText('Número de nodo local')

        self.lineEditNodoKant.setToolTip('Número de nodo asignado al nodo local para\n'
                                      'informar al Kant cliente del estado del mismo')

    def createConfigKeepAliveGroupBox(self):
        self.GroupBoxKeepAlive = QtWidgets.QGroupBox(self.tab7)
        self.GroupBoxKeepAlive.setGeometry(QtCore.QRect(15, 170, 460, 100))
        self.GroupBoxKeepAlive.setObjectName("GroupBoxKeepAlive")

        # Segundos para prevencion
        self.labelSegsBAPAlive = QtWidgets.QLabel(self.GroupBoxKeepAlive)
        self.labelSegsBAPAlive.setGeometry(QtCore.QRect(20, 20, 130, 16))
        self.labelSegsBAPAlive.setObjectName("labelSegsBAPAlive")

        self.spinBoxSegsBAPAlive = QtWidgets.QSpinBox(self.GroupBoxKeepAlive)
        self.spinBoxSegsBAPAlive.setGeometry(QtCore.QRect(170, 20, 40, 20))
        self.spinBoxSegsBAPAlive.setObjectName("spinBoxSegsBAPAlive")

        # Num. Alives para normalizacion
        self.labelNumBAPAlive = QtWidgets.QLabel(self.GroupBoxKeepAlive)
        self.labelNumBAPAlive.setGeometry(QtCore.QRect(20, 45, 140, 16))
        self.labelNumBAPAlive.setObjectName("labelNumBAPAlive")

        self.spinBoxNumBAPAlive = QtWidgets.QSpinBox(self.GroupBoxKeepAlive)
        self.spinBoxNumBAPAlive.setGeometry(QtCore.QRect(170, 45, 40, 20))
        self.spinBoxNumBAPAlive.setObjectName("spinBoxNumBAPAlive")

        # Enviar Status IO
        self.labelStatusBAPConfig = QtWidgets.QLabel(self.GroupBoxKeepAlive)
        self.labelStatusBAPConfig.setGeometry(QtCore.QRect(20, 70, 110, 16))
        self.labelStatusBAPConfig.setObjectName("labelStatusBAPConfig")

        self.comboBoxStatusBAPAlive = QtWidgets.QComboBox(self.GroupBoxKeepAlive)
        self.comboBoxStatusBAPAlive.setGeometry(QtCore.QRect(150, 70, 60, 20))
        self.comboBoxStatusBAPAlive.setEditable(False)
        self.comboBoxStatusBAPAlive.setObjectName("comboBoxStatusBAPAlive")
        self.comboBoxStatusBAPAlive.addItem("")
        self.comboBoxStatusBAPAlive.addItem("")

        # Check Interval
        self.labelCheckBAPConfig = QtWidgets.QLabel(self.GroupBoxKeepAlive)
        self.labelCheckBAPConfig.setGeometry(QtCore.QRect(255, 20, 80, 20))
        self.labelCheckBAPConfig.setObjectName("labelCheckBAPConfig")

        self.spinBoxCheckBAPConfig = QtWidgets.QSpinBox(self.GroupBoxKeepAlive)
        self.spinBoxCheckBAPConfig.setGeometry(QtCore.QRect(395, 20, 40, 20))
        self.spinBoxCheckBAPConfig.setObjectName("spinBoxCheckBAPConfig")

        # Default Test Time
        self.labelDefaultBAPConfig = QtWidgets.QLabel(self.GroupBoxKeepAlive)
        self.labelDefaultBAPConfig.setGeometry(QtCore.QRect(255, 45, 105, 20))   # CHEQUEAR ESTE VALOR
        self.labelDefaultBAPConfig.setObjectName("labelDefaultBAPConfig")

        self.spinBoxDefaultBAPConfig = QtWidgets.QSpinBox(self.GroupBoxKeepAlive)
        self.spinBoxDefaultBAPConfig.setGeometry(QtCore.QRect(395, 45, 40, 20))
        self.spinBoxDefaultBAPConfig.setObjectName("spinBox2BAPConfig")

        # Auto Update Params
        self.labelAutoBAPAlive = QtWidgets.QLabel(self.GroupBoxKeepAlive)
        self.labelAutoBAPAlive.setGeometry(QtCore.QRect(255, 70, 115, 16))
        self.labelAutoBAPAlive.setObjectName("labelAutoBAPAlive")

        self.comboBoxAutoBAPAlive = QtWidgets.QComboBox(self.GroupBoxKeepAlive)
        self.comboBoxAutoBAPAlive.setGeometry(QtCore.QRect(375, 70, 60, 20))
        self.comboBoxAutoBAPAlive.setEditable(False)
        self.comboBoxAutoBAPAlive.setObjectName("comboBoxAutoBAPAlive")
        self.comboBoxAutoBAPAlive.addItem("")
        self.comboBoxAutoBAPAlive.addItem("")

        # Configuracion BAPKeepAlive
        self.GroupBoxKeepAlive.setTitle('Configuración BAPKeepAlive')
        self.comboBoxStatusBAPAlive.setCurrentText("True")
        self.comboBoxStatusBAPAlive.setItemText(0, "True")
        self.comboBoxStatusBAPAlive.setItemText(1, "False")
        self.labelStatusBAPConfig.setText("Enviar STATUS_IO")
        self.labelNumBAPAlive.setText("Num. alives para norm.")
        self.labelSegsBAPAlive.setText("Segs. para prevención")
        self.labelDefaultBAPConfig.setText("Default Test Time")
        self.labelAutoBAPAlive.setText("AutoUpdate Params")
        self.comboBoxAutoBAPAlive.setCurrentText("True")
        self.comboBoxAutoBAPAlive.setItemText(0, "True")
        self.comboBoxAutoBAPAlive.setItemText(1, "False")
        self.labelCheckBAPConfig.setText("Check Interval")

        self.labelCheckBAPConfig.setToolTip('Intervalo que se chequea la cola en segundos')
        self.spinBoxCheckBAPConfig.setToolTip('Intervalo que se chequea la cola en segundos')

        self.labelDefaultBAPConfig.setToolTip('Cada cuántos segundos la placa BAP debe transmitir un evento BAP ALIVE')
        self.spinBoxDefaultBAPConfig.setToolTip('Cada cuántos segundos la placa BAP debe transmitir un evento BAP ALIVE')

        self.labelSegsBAPAlive.setToolTip('Tiempo que se espera desde la última comunicación con la placa BAP\n'
                                       'para considerarla en prevención. Debe ser mayor o igual a Check Interval\n'
                                       'sino siempre se encontraran en prevención')
        self.spinBoxSegsBAPAlive.setToolTip('Tiempo que se espera desde la última comunicación con la placa BAP\n'
                                         'para considerarla en prevención. Debe ser mayor o igual a Check Interval\n'
                                         'sino siempre se encontraran en prevención')

        self.labelNumBAPAlive.setToolTip('Cantidad de veces que debe reportarse como normal una placa BAP para\n'
                                       'considerarla normalizada luego de haber entrado en prevención')
        self.spinBoxNumBAPAlive.setToolTip('Cantidad de veces que debe reportarse como normal una placa BAP para\n'
                                         'considerarla normalizada luego de haber entrado en prevención')

        self.comboBoxStatusBAPAlive.setToolTip('Indica si se envía un comando STATUS_IO a las placas BAP para\n'
                                          'que informen su estado. Si no se envía STATUS_IO igualmente\n'
                                          'pueden enviarse "Auto Update Params"')
        self.labelStatusBAPConfig.setToolTip('Indica si se envía un comando STATUS_IO a las placas BAP para\n'
                                        'que informen su estado. Si no se envía STATUS_IO igualmente\n'
                                        'pueden enviarse Auto Update Params"')

        self.comboBoxAutoBAPAlive.setToolTip('Indica si se debe enviar los parámetros automáticamente cuando\n'
                                          'se logra la primer comunicación con la placa BAP.')
        self.labelAutoBAPAlive.setToolTip('Indica si se debe enviar los parámetros automáticamente cuando\n'
                                       'se logra la primer comunicación con la placa BAP.')


# # No se ejecuta
# if __name__ == "__main__":
#     app = QtWidgets.QApplication([])
#     MainWindow = QtWidgets.QWidget()
#     ui = Ui_MainWindow()
#     MainWindow.show()
#     sys.exit(app.exec_())


