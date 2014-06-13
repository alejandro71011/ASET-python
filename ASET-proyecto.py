import datetime
Identificador=0
class Asociado:
    __nombre=""
    __cedula=0
    __puesto=""
    __departamento=""
    __direccion=""
    __telefono=0
    __correo=""
    __nacimiento=0
    __fecingreso=0
    __estado=""
    __ingmensual=0
    __egmensual=0

    def __init__(self, cedula, correo, departamento, direccion, egmensual, estado, fecingreso, ingmensual, nacimiento, nombre, puesto, telefono):
        self.__nombre = nombre
        if 99999999>=cedula>1000000:
            self.__cedula = cedula
        self.__puesto = puesto
        self.__departamento = departamento
        self.__direccion = direccion
        if 89999999>=telefono>2000000:
            self.__telefono = telefono
        if ("@" in correo==True) and (".com" in correo==True):
            self.__correo = correo
        self.__nacimiento = nacimiento
        self.__fecingreso = fecingreso
        if estado.upper()=="A" or estado.upper()=="I":
            self.__estado = estado
        if ingmensual>=0:
            self.__ingmensual = ingmensual
        if egmensual>=0:
            self.__egmensual = egmensual
        self.__TiposdeCredito=[]

    def getNombre(self):
        return self.__nombre
    def setNombre(self, nombre):
        self.__nombre = nombre

    def getCedula(self):
        return self.__cedula
    def setCedula(self, cedula):
        if 99999999>=cedula>1000000:
            self.__cedula = cedula

    def getPuesto(self):
        return self.__puesto
    def setPuesto(self, puesto):
        self.__puesto = puesto

    def getDepartamento(self):
        return self.__departamento
    def setDepartamento(self, departamento):
        self.__departamento = departamento

    def getDireccion(self):
        return self.__direccion
    def setDireccion(self, direccion):
        self.__direccion = direccion

    def getTelefono(self):
        return self.__telefono
    def setTelefono(self, telefono):
        if 89999999>=telefono>2000000:
            self.__telefono = telefono

    def getCorreo(self):
        return self.__correo
    def setCorreo(self, correo):
        if "@" in correo==True:
            self.__correo = correo

    def getNacimiento(self):
        return self.__nacimiento
    def setNacimiento(self, nacimiento):
        self.__nacimiento = nacimiento2

    def getFecingreso(self):
        return self.__fecingreso
    def setFecingreso(self, fecingreso):
        self.__fecingreso = fecingreso

    def getEstado(self):
        return self.__estado
    def setEstado(self, estado):
        if estado.upper()=="A" or estado.upper()=="I":
            self.__estado = estado

    def getIngmensual(self):
        return self.__ingmensual
    def setIngmensual(self, ingmensual):
        if ingmensual>=0:
            self.__ingmensual = ingmensual

    def getEgmensual(self):
        return self.__egmensual
    def setEgmensual(self, egmensual):
        if egmensual>=0:
            self.__egmensual = egmensual

    def ahorrObrero(self):
        return self.getIngMensual()*0.5

    def ahorroPatronal(self):
        return self.getIngMensual()*0.2

    def capacidadPago(self):
        capacidad=self.getEgmensual()/self.getIngMensual()
        return capacidad>=0.35


pass

class Credito:
    __identificador=0
    __plazodepago=0
    __dinerosolici=0
    __rsolicitud=""
    __fechaprob=0
    __fechapago=0
    __asociado=None
    __tipoCredito=None
    montoAbonado=0

    def __init__(self, dinerosolicitado, fechapago, fechaprob, identificador, plazodepago, asociado, tipoCredito):
        self.__identificador = identificador
        self.__tipoCredito = tipoCredito
        self.__asociado = asociado
        if dinerosolicitado>0:
            self.__dinerosolicitado = dinerosolicitado
        if (self.montoMaximo() < dinerosolicitado):
            self.__rsolicitud = "R"
        else:
            self.__rsolicitud = "A"
        if self.__rsolicitud=="A":
            self.__fechaprob = fechaprob
        else:
            self.__fechaprob=0
        if self.__rsolicitud=="A":
            self.__fechapago = fechapago
        else:
            self.__fechapago=0

    def montoMaximo(self):
        monto = self.getTipoCredito().getMontoMaximo()
        if (monto == 0):
            monto = self.getAsociado().getAhorroObrero();
        return monto


    def getIdentificador(self):
        return self.__identificador
    def setIdentificador(self, identificador):
        self.__identificador = identificador

    def getAsociado(self):
        return self.__asociado
    def setAsociado(self, asociado):
        self.__asociado = asociado

    def getTipoCredito(self):
        return self.__tipoCredito
    def setTipocredito(self, asociado):
        self.__tipoCredito = tipoCredito

    def getDinerosolicitado(self):
        return self.__dinerosolicitado
    def setDinerosolicitado(self, dinerosolicitado):
        if dinerosolicitado>0:
            self.__dinerosolicitado = dinerosolicitado

    def getRsolicitud(self):
        return self.__rsolicitud

    def getFechaprob(self):
        return self.__fechaprob
    def setFechaprob(self, fechaprob):
        if rsolicitud=="A":
            self.__fechaprob = fechaprob
        else:
            self.__fechaprob=0

    def getFechadepago(self):
        return self.__fechadepago
    def setFechadepago(self,fechadepago):
        if rsolicitud=="A":
            self.__fechadepago = fechadepago
        else:
            self.__fechapago=0

    def setPlazodepago(self,plazodepago):
        if rsolicitud=="A":
            self.__plazodepago = plazodepago
        else:
            self.__fechapago=0
    def getPlazodepago(self):
        return self.__plazodepago

    def pagoMensual(self):
        if self.__rsolicitud=="A":
            pasoA = (self.getTipoCredito().getInteresAnual() / 100) / 12
            pasoB = pasoA + 1
            pasoC = pasoB**(self.getPlazodepago() * -1)
            pasoD = 1 - pasoC
            pasoE = pasoA * self.getDinerosolicitado()
            return pasoE / pasoD
        else:

            print("Credito rechazado por la junta")

    def cuotaMensual(self,monto,plazo,tasa):
        cuota=(monto*(((tasa/100)*(tasa/100))*(plazo/12)))/((1+(tasa/100))*((plazo/12)-1))
        interes=monto*tasa
        amortizacion=cuota-interes
        print("Cuota Mensual: " + str(cuota))
        print("Interes: " + str(interes))
        print("Amortizacion: " + str(amortizacion))
        return cuota

    def abonar(self):
        montoAbonado = montoAbonado + monto
        saldo = self.totalPago() - montoAbonado
        return saldo

    def obtenerSaldo(self):
        return self.totalPago() - montoAbonado

    def totalPago(self):
        return self.pagoMensual() * self.getPlazodepago()

    def mesesMorosos(self):
        fechaAprob = self.getFechaprob()
        fecha = datetime.datetime.strptime(fechaAprob, "%d/%m/%Y").date()
        hoy = datetime.datetime.now().date()
        dif = fecha - hoy
        meses = dif.days / 30
        return meses - (meses * (self.montoAbonado / (meses * self.pagoMensual())))


pass

class TipoCredito:
    __identificador=0
    __montoMaximo=0
    __plazoMaximo=0
    __interesAnual=0
    __nombre=""

    def __init__(self, identificador, interesAnual, montoMaximo, plazoMaximo,nombre):
        self.__identificador = identificador
        self.__montoMaximo = montoMaximo
        self.__plazoMaximo = plazoMaximo
        self.__interesAnual = interesAnual
        self.__nombre=nombre

    def getInteresAnual(self):
        return self.__interesAnual
    def getIdentificador(self):
        return self.__identificador
    def getMontoMaximo(self):
       return self.__montoMaximo
    def getPlazoMaximo(self):
        return self.__plazoMaximo
    def getNombre(self):
        return self.__nombre

    def setInteresAnual(self, interesAnual):
        self.__interesAnual = interesAnual
    def setIdentificador(self, identificador):
        self.__identificador = identificador
    def setMontoMaximo(self, montoMaximo):
        self.__montoMaximo = montoMaximo
    def setPlazoMaximo(self, plazoMaximo):
        self.__plazoMaximo = plazoMaximo
    def setNombre(self,nombre):
        self.__nombre = nombre

pass


class Aset:
    asociados = []
    creditos = []
    TiposdeCredito=[]

    def __init__(self):
        self.asociados=[]
        self.creditos=[]
        self.__TiposdeCredito=[]

    def buscarAsociado(self,cedula):
        for asociado in self.asociados:
            if asociado.getCedula() == cedula:
                return asociado
            else:
                print("Asociado no existe")
            return None

    def sociosActivos(self):
        count = 0
        for asociado in self.asociados:
            if asociado.getEstado().upper() == 'A':
                count=count+1
                print(asociado.getNombre())
        print("Encontrados " + str(count) + " socios activos")

    def sociosInactivos(self):
        count = 0
        for asociado in self.asociados:
            if asociado.getEstado().upper() == 'I':
                count=count+1
                print(asociado.getNombre())
        print("Encontrados " + str(count) + " socios inactivos")


    def buscarCredito(self,identificador):
        for credito in self.creditos:
            if credito.getIdentificador() == identificador:
                return credito
            return None

    def eliminarAsociado(self,cedula):
        asociado = buscarAsociado(cedula)
        asociados.remove(asociado)

    def eliminarCredito(self,identificador):
        credito = buscarCredito(identificador)
        creditos.remove(credito)

    def capacidadPago(self,cedula):
        asociado = buscarAsociado(cedula)
        return asociado.capacidadPago()

    def pagoMensual(self,identificador):
        credito = self.buscarCredito(identificador)
        return credito.pagoMensual();

    def abonarCredito(self,cedula, identificador, monto):
        credito = self.buscarCredito(identificador)
        return credito.abonar(monto)

    def obtenerSaldo(self,cedula, identificador):
        credito = self.buscarCredito(identificador)
        return credito.obtenerSaldo()

    def cuotaMensual(self,identificador,monto,plazo,tasa):
        credito = self.buscarCredito(identificador)
        return credito.cuotaMensual(monto,plazo,tasa)



    def mesesCancelacion(self):
        fechaAprobStr = Credito.getFechaprob()
        fechaAprob = datetime.datetime.strptime(fechaAprobStr, "%d/%m/%Y").date()
        fechaPagoStr = Credito.getFechapago()
        fechaPago = datetime.datetime.strptime(fechaPagoStr, "%d/%m/%Y").date()
        dif = fechaAprob - fechaPago
        return dif.days / 30

    def clientesMorosos(self):
        morosos = []
        for credito in self.creditos:
            mesesMorosos = credito.mesesMorosos()
            if mesesMorosos > 1:
                morosos.append(credito.getAsociado())
                print "\rCedula: " + str(credito.getAsociado().getCedula())
                print "Nombre: " + credito.getAsociado().getNombre()
                print "Tipo de prestamo: " + credito.getTipoCredito().nombreTipoCredito()
                print "Pago Mensual: " + str(credito.pagoMensual())
                print "Meses Adeudados: " + str(mesesMorosos)
                print "Total Adeudado: " + str(mesesMorosos * credito.pagoMensual())
        print("Encontrados " + str(len(morosos)) + " asociados morosos")
        return morosos

    def clientesConPrestamo(self):
        conPrestamo = []
        for credito in creditos:
            conPrestamo.append(credito.getAsociado())
            print "\rCedula: " + str(credito.getAsociado().getCedula())
            print "Nombre: " + credito.getAsociado().getNombre()
            print "Tipo de prestamo: " + credito.getTipoCredito().nombreTipoCredito()
            print "Dinero Solicitado: " + str(credito.
                                              getDinerosolicitado())
            print "Saldo Actual: " + str(credito.obtenerSaldo())
        print("Encontrados " + str(len(conPrestamo)) + " clientes con prestamo")
        return conPrestamo


    def montoPorDepartamento(self):
        departamentos = {}
        for credito in creditos:
            departamento = credito.getAsociado().getDepartamento()
            if not(departamentos.has_key(departamento)):
                departamentos[departamento] = 0
            departamentos[departamento] = departamentos[departamento] + credito.getDinerosolicitado()
        for departamento in departamentos.keys():
            print departamento + " " + str(departamentos[departamento])
        return departamentos

    def montoPorTipo(self):
        tipos= {}
        for credito in self.creditos:
            tipo = credito.getIdentificador()
            if(not tipos.has_key(tipo)):
                tipos[tipo] = 0
            tipos[tipo] = tipos[tipo] + credito.getDinerosolicitado()
        for tipo in tipos.keys():
            print tipo + " " + str(tipos[tipo])
        return tipos

    def montoPorAnho(self):
        anhos= {}
        for credito in self.creditos:
            fechaAprob = credito.getFechaprob()
            fecha = datetime.datetime.strptime(fechaAprob, "%d/%m/%Y").date()
            anho = fecha.year
            if(not anhos.has_key(anho)):
                anhos[anho] = 0
            anhos[anho] = anhos[anho] + credito.getDinerosolicitado()
        for anho in anhos.keys():
            print str(anho) + " " + str(anhos[anho])
        return anhos

    def prestamosMasAltos(self):
        todos = []
        masAltos = []
        for credito in self.creditos:
            todos.append(credito.getDinerosolicitado())
        for i in range(0, 10):
            mayor = max(todos)
            masAltos.append(mayor)
            todos.remove(mayor)
            print str(mayor)
        return masAltos

    def clientesCancelaronAntes():
        clientes = []
        for credito in self.creditos:
            meses = credito.mesesCancelacion()
            if meses > 0:
                clientes.append(credito.getAsociado())
                print "\rCedula: " + str(credito.getAsociado().getCedula())
                print "Nombre: " + credito.getAsociado().getNombre()
                print "Tipo de prestamo: " + credito.getTipoCredito().nombreTipoCredito()
                print "Meses en los que cancelo el prestamo: " + str(meses)
        print("Encontrados " + str(len(clientes)) + " clientes que pagaron antes del plazo de pago")
        return clientes

pass

#OBJETOS FUERA DE CLASE
aset=Aset()
ppordinario=TipoCredito(0,9.75,0, 30,"Prestamo Personal Ordinario")
aset.TiposdeCredito.append(ppordinario)
ppinversion=TipoCredito(1,15.75,10000000,84,"Prestamo Personal Inversion")
aset.TiposdeCredito.append(ppinversion)
ppvivienda=TipoCredito(2,9.75,5000000,60,"Prestamo Personal VIvienda")
aset.TiposdeCredito.append(ppvivienda)
ppeducacion=TipoCredito(3,9.75,3000000,24,"Prestamo Personal Educacion")
aset.TiposdeCredito.append(ppeducacion)
ppsalud=TipoCredito(4,9.75,3000000,24,"Prestamo Personal Salud")
aset.TiposdeCredito.append(ppsalud)

asociado1=Asociado(20710712, "m@m.com", "computacion", "florencia", 35000, "A", "12/06/2009", 200000, "14/05/1987", "Maren", "profesor", 88888888)
aset.asociados.append(asociado1)

credito1=Credito(1000000, "12/06/2015", "12/06/2014", 0, 12, asociado1, ppinversion)
aset.creditos.append(credito1)


while 1:
    menu=input("Bienvenido al sistema de creditos ASET! \rDigite: \r1.Para gestionar Asociados."+
           "\r2.Para gestionar creditos. \r3.Para obtener reportes. \r\rCualquier otro numero para salir del programa.\r")
    if menu==1:
        while 1:
            menu1=input("Gestion Asociados: \rDigite: \r1.Para agregar asociado. \r2.Para editar asociado. \r3.Para eliminar asociado. \r4.Para ver la informacion de algun asociado."+
                "\r\rCualquier otro numero para volver al menu principal.\r")
            if menu1==1:
                nombre=raw_input("Digite el nombre completo del nuevo asociado")
                cedula=int(raw_input("Digite el numero de cedula (unicamente numeros)"))
                puesto=raw_input("Digite el puesto de trabajo")
                departamento=raw_input("Digite el departamento en que trabaja")
                direccion=raw_input("Digite la direccion de residencia")
                telefono=int(raw_input("Digite el numero de telefono(unicamente numeros)"))
                correo=raw_input("Digite el correo electronico")
                nacimiento=raw_input("Digite la fecha de nacimiento")
                fecingreso=raw_input("Digite la fecha en que ingreso a ASET")
                estado=raw_input("Digite A si es un asociado activo, de lo contario digite I")
                ingmensual=int(raw_input("Digite el ingreso mensual"))
                egmensual=int(raw_input("Digite el egreso mensual\r"))

                asociado1=Asociado(cedula, correo, departamento, direccion, egmensual, estado, fecingreso, ingmensual, nacimiento, nombre, puesto, telefono)
                aset.asociados.append(asociado1)
                print(str(aset.asociados[len(aset.asociado-1)].getNombre())+"\r")

            elif menu1==2:
                cedula=input("Por favor digite la cedula")
                for asociado in aset.asociados:
                    if asociado.getCedula() == cedula:
                        while 1:
                            cambio=input("Digite: \r1.Para editar el puesto. \r2.Para editar el departamento. \r3.Para editar la direccion."
                                     +"\r4.Para editar el telefono. \r5.Para editar el correo. \r6.Para editar el estado.\r7.Para editar el ingreso mensual."
                                     +"\r8.Para editar el egreso mensual \rCualquier otro numero para volver al menu de gestion asociados\r")
                            if cambio==1:
                                puesto=raw_input("Digite el puesto de trabajo")
                                asociado.setPuesto(puesto)
                            elif cambio==2:
                                departamento=raw_input("Digite el departamento en que trabaja")
                                asociado.setDepartamento(departamento)
                            elif cambio==3:
                                direccion=raw_input("Digite la direccion de residencia")
                                asociado.setDireccion(direccion)
                            elif cambio==4:
                                telefono=int(raw_input("Digite el numero de telefono(unicamente numeros)"))
                                asociado.setTelefono(telefono)
                            elif cambio==5:
                                correo=raw_input("Digite el correo electronico")
                                asociado.setCorreo(correo)
                            elif cambio==6:
                                estado=raw_input("Digite A si es un asociado activo, de lo contario digite I")
                                asociado.setEstado(estado)
                            elif cambio==7:
                                ingmensual=int(raw_input("Digite el ingreso mensual"))
                                asociado.setIngmensual(ingmensual)
                            elif cambio==8:
                                egmensual=int(raw_input("Digite el egreso mensual"))
                                asociado.setEgmensual(egmensual)
                            else:
                                break

            elif menu1==3:
                cedula=input("Digite el numero de cedula")
                aset.eliminarAsociado(cedula)
            elif menu1==4:
                cedula=input("Digite la cedula del asociado")
                aset.buscarAsociado(cedula)
            else:
                break

    elif menu==2:
        while 1:
            menu2=input("Gestion Creditos: \rDigite: \r1.Para asignar un credito. \r2.Para editar un credito."
                        +"\r3.Para eliminar un credito. \r4.Para ver la informacion de un credito."+
                "\r5.Para ver el saldo de un credito. \r6.Para abonar a un credito. \r7.Para calcular el pago mensual."
                +"\r8.Para calcular la cuota mensual. \r9.Para agregar un tipo de credito. \r\rCualquier otro numero para volver al menu principal.\r")
            if menu2==1:
                identificador=Identificador+1
                Identificador=identificador
                cedula=int(raw_input("Digite la cedula del asociado"))
                print ("Tipos de credito disponibles")
                con=1
                for credito in aset.TiposdeCredito:
                    print(str(con)+". " + credito.getNombre())
                    con = con + 1
                tipoCredito=int(raw_input("Seleccione el tipo de credito utilizando el numero"))
                plazodepago=int(raw_input("Digite el plazo en que se desea pagar"))
                dinerosolicitado=int(raw_input("Digite la cantidad de dinero a solicitar"))
                rsolicitud=raw_input("Digite A si fue aprobada, de lo contrario digite R")
                fechaprob=(raw_input("Digite la fecha en que se aprobo"))
                fechadepago=(raw_input("Digite la fecha de pago"))

                c=aset.TiposdeCredito[tipoCredito-1]
                asociado=None
                for socio in aset.asociados:
                    if cedula == socio.getCedula():
                        asociado = socio
                if c != None and asociado != None:
                    credito1=Credito(dinerosolicitado, fechadepago, fechaprob, identificador, plazodepago, asociado, c)
                    aset.creditos.append(credito1)
                    print(aset.creditos[len(aset.creditos-1)].getCedula())
                    print(aset.creditos[len(aset.creditos-1)].getIdentificador())

            elif menu2==2:
                identificador=input("Por favor digite el identificador")
                for credito in creditos:
                    if credito.getIdentificador() == identificador:

                        while 1:

                            cambio=input("Digite: \r1.Para editar el tipo de credito. \r2.Para editar el plazo de pago. \r3.Para editar el dinero solicitado."
                                     +"\r4.Para editar la fecha de pago. \rCualquier otro numero para volver al menu de gestion creditos\r")
                            if cambio==1:
                                tipoCredito=raw_input("Digite el tipo de credito")


                                asociado.setTipocredito(tipoCredito)
                            elif cambio==2:
                                plazodepago=int(raw_input("Digite el plazo de pago"))
                                asoc
                                iado.setPlazodepago(plazodepago)
                            elif cambio==3:
                                dinerosolicitado=int(raw_input("Digite el dinero solicitado"))
                                asociado.setDinerosolicitado(dinerosolicitado)
                            elif cambio==4:
                                fechapago=int(raw_input("Digite la fecha de pago"))
                                asociado.setFechadepago(fechadepago)
                            else:
                                break

            elif menu2==3:
                identificador=input("Digite el numero de identificador")
                aset.eliminarCredito(identificador)
            elif menu2==4:
                identificador=input("Digite el identificador del prestamo")
                aset.buscarCredito(identificador)

            elif menu2==5:
                identificador=input("Digite el numero de identificador")
                cedula=input("Digite el numero de cedula")
                aset.obtenerSaldo(cedula, identificador)
            elif menu2==6:
                cedula=input("Digite la cedula")
                identificador=input("Digite el identificador del prestamo")
                monto=input("Digite el monto que se abonara")
                aset.abonarCredito(cedula,identificador,monto)

            elif menu2==7:
                identificador=input("Digite el identificador del prestamo")
                for credito in aset.creditos:
                    if credito.getIdentificador() == identificador:
                        aset.pagoMensual()

            elif menu2==8:
                monto=input("Digite el monto a solicitar")
                plazo=input("Digite el plazo estimado para pagar")
                tasa=input("Digite la tasa de interes")
                aset.cuotaMensual(monto,plazo,tasa)

            elif menu2==9:
                identificador=aset.TiposdeCredito[len(aset.TiposdeCreditos)]
                interesAnual=input("Digite la tasa basica pasiva")
                montoMaximo=input("Digite el monto maximo disponible")
                plazoMaximo=input("Digite el plazo maximo disponible")
                nombre=raw_input("Digite el nombre del credito")

                tiponuevo=TipoCredito(identificador, interesAnual, montoMaximo, plazoMaximo,nombre)
                aset.TiposdeCredito.append(tiponuevo)
                print(aset.TiposdeCredito[len(aset.TiposdeCreditos-1)].getNombre())

            else:
                break

    elif menu==3:
        while 1:
            menu3=input("Reportes: \rDigite: \r1.Para obtener la lista de los socios activos. \r2.Para obtener la lista de los socios inactivos."
                        +"\r3.Para obtener los tipos de creditos disponibles en ASET. \r4.Para obtener la lista de los asociados morosos."+
                "\r5.Para obtener lista de asociados con prestamos pendientes. \r6.Para obtener el monto total de los creditos otorgados."
                +"\r7.Para obtener el monto total de creditos otorgados por tipo de prestamo. \r8. Para obtener el monto total de creditos otorgados por ano."
                +"\r9. Para mostrar los 10 prestamos de mayor monto."+"\r10. Para obtener los clientes que cancelaron un prestamo antes del plazo de pago"
                +"\r\rCualquier otro numero para volver al menu principal.\r")

            if menu3==1:
                aset.sociosActivos()

            elif menu3==2:
                aset.sociosInactivos()

            elif menu3==3:
                #reviasr
                for TCredito in aset.TiposdeCredito:
                    print TCredito.getNombre()

            elif menu3==4:
                aset.clientesMorosos()

            elif menu3==5:
                aset.clientesConPrestamo()

#            elif menu3==6: <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

            elif menu3==7:
                aset.montoPorTipo()

            elif menu3==8:
                aset.montoPorAnho()

            elif menu3==9:
                aset.prestamosMasAltos()

            elif menu3==10:
                aset.clientesCancelaronAntes()

            else:
                break



    else:
        print("Esperamos que haya logrado lo que esperaba exitosamente,\rGracias por preferirnos,\rHasta luego! \r\rA.R. Software Company")
        break