from dataclasses import dataclass
from distutils.util import run_2to3
from tabnanny import check
from PySide2.QtWidgets import QWidget
from views.main_window import Modelo
from main import LogisticRegressionEmpleados, LogisticRegressionTurnos
from PySide2.QtCore import Qt

class ModelWindow(QWidget, Modelo):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.InputButton.clicked.connect(self.adddata)
        #self.InputButton.clicked.connect(self.adddata_turnos)
        self.frameInput.setStyleSheet("border: 1px solid black;")
        self.frameOutput.setStyleSheet("border: 1px solid black;")
        self.frameModelo.setStyleSheet("border: 1px solid black;")
        self.Model.setStyleSheet("color: red;")
        self.ErrorEmp.setStyleSheet("color: red;")
        self.ErrorTur.setStyleSheet("color: red;")
        self.ErrorEq1.setStyleSheet("color: red;")
        self.ErrorEq2.setStyleSheet("color: red;")
        self.ErrorEq3.setStyleSheet("color: red;")
        self.ErrorEq4.setStyleSheet("color: red;")

#Analisis con Empleados
    def check_data(self):
        empleados = self.EmployeeNumberInput.value()
        turnos = self.MonthShiftInput.value()
        r1 = self.Req1Input.value()
        r2 = self.Req2Input.value()
        r3 = self.Req3Input.value()
        r4 = self.Req4Input.value()

        errors_count = 0
        
        if empleados <= 0 and turnos <= 0:
            self.ErrorEmp.setText("Error: Ingrese un valor superior a 0")
            self.ErrorTur.setText("Error: Ingrese un valor superior a 0")
            errors_count += 1
        else:
            self.ErrorEmp.clear()
            self.ErrorTur.clear()
        if r1 <= 0:
            self.ErrorEq1.setText("Error: Ingrese un valor superior a 0")
            errors_count += 1
        else:
            self.ErrorEq1.clear()
        if r2 <= 0:
            self.ErrorEq2.setText("Error: Ingrese un valor superior a 0")
            errors_count += 1
        else:
            self.ErrorEq2.clear()
        if r3 <= 0:
            self.ErrorEq3.setText("Error: Ingrese un valor superior a 0")
            errors_count += 1
        else:
            self.ErrorEq3.clear()
        if r4 <= 0:
            self.ErrorEq4.setText("Error: Ingrese un valor superior a 0")
            errors_count += 1
        else:
            self.ErrorEq4.clear() 
        if errors_count == 0:
            return True
    
    def adddata(self):
        empleados = self.EmployeeNumberInput.value()
        turnos = self.MonthShiftInput.value()
        r1 = self.Req1Input.value()
        r2 = self.Req2Input.value()
        r3 = self.Req3Input.value()
        r4 = self.Req4Input.value()

        if self.check_data():
            if empleados <= 0:
                data = (turnos, r1, r2, r3, r4)
                ModeloPredictivo = LogisticRegressionTurnos(data)
                aTexto = str(ModeloPredictivo)
                characters = "[']"
                for x in range(len(characters)):
                    aTexto = aTexto.replace(characters[x],"")
                self.Model.setText(aTexto)
            if turnos <= 0:
                data = (empleados, r1, r2, r3, r4)
                ModeloPredictivo = LogisticRegressionEmpleados(data)
                aTexto = str(ModeloPredictivo)
                characters = "[']"
                for x in range(len(characters)):
                    aTexto = aTexto.replace(characters[x],"")
                self.Model.setText(aTexto)
"""
#Analisis Turnos
    def check_data_turnos(self):
        turnos = self.MonthShiftInput.value()
        r1 = self.Req1Input.value()
        r2 = self.Req2Input.value()
        r3 = self.Req3Input.value()
        r4 = self.Req4Input.value()

        errors_count = 0
        
        if turnos <= 0:
            self.ErrorTur.setText("Error: Ingrese un valor superior a 0")
            errors_count += 1
        else:
            self.ErrorTur.clear()
            self.ErrorEmp.clear()
        if r1 <= 0:
            self.ErrorEq1.setText("Error: Ingrese un valor superior a 0")
            errors_count += 1
        else:
            self.ErrorEq1.clear()
        if r2 <= 0:
            self.ErrorEq2.setText("Error: Ingrese un valor superior a 0")
            errors_count += 1
        else:
            self.ErrorEq2.clear()
        if r3 <= 0:
            self.ErrorEq3.setText("Error: Ingrese un valor superior a 0")
            errors_count += 1
        else:
            self.ErrorEq3.clear()
        if r4 <= 0:
            self.ErrorEq4.setText("Error: Ingrese un valor superior a 0")
            errors_count += 1
        else:
            self.ErrorEq4.clear() 
        if errors_count == 0:
            return True
    
    def adddata_turnos(self):
        turnos = self.MonthShiftInput.value()
        r1 = self.Req1Input.value()
        r2 = self.Req2Input.value()
        r3 = self.Req3Input.value()
        r4 = self.Req4Input.value()

        if self.check_data_turnos():
            data = (turnos, r1, r2, r3, r4)
            ModeloPredictivo = LogisticRegressionTurnos(data)
            aTexto = str(ModeloPredictivo)
            characters = "[']"
            for x in range(len(characters)):
                aTexto = aTexto.replace(characters[x],"")
            self.Model.setText(aTexto)
            """