class Aereopuerto:
    
    # Atributos privados
    __id=None
    __airportName=None
    __city=None
    __country=None
    __IATACode=None
    __ICAOCode=None
    __latitude=None
    __longitude=None
    __altitude=None
    __UTCTimeZone=None
    __DST=None
    __continentState=None
    __hemisferio=None
    __nativeName="Sin nombre nativo"
    
    # Constructor de clase
    def __init__(self,id=None,airportName=None,city=None,country=None,IATACode=None,ICAOCode=None,latitude=None,longitude=None,altitude=None,UTCTimeZone=None,DST=None,continentState=None,nativeName="Sin nombre nativo"):
        
        self.__id = id
        self.__airportName = airportName
        self.__city = city
        self.__country = country
        self.__IATACode = IATACode
        self.__ICAOCode = ICAOCode
        self.__latitude = latitude
        self.__longitude = longitude
        self.__altitude = altitude
        self.__UTCTimeZone = UTCTimeZone
        self.__DST = DST
        self.__continentState = continentState
        
        # Función para saber el Hemisferio al que pertenece el Aereopuerto.
        self.__hemisferio = "Hemisferio Norte" if float(self.__latitude)>0 else "Hemisferio Sur"
        
        self.__nativeName = nativeName
        
    # Redefinimos el método string
    def __str__(self):
        return ("id: {} \nAirport Name: {} \nCity: {} \nCountry: {} \nIATA Code: {} \nICAO Code: {} \n"
            "Latitude: {} \nLongitude: {} \nAltitude: {} \nUTC TimeZone: {} \nDST: {} \nContinent/State: {} \n"
            "El aereopuerto se encuentra en el: {} \n".format(
                self.__id,self.__airportName,self.__city, self.__country, self.__IATACode, self.__ICAOCode,
                self.__latitude, self.__longitude, self.__altitude, self.__UTCTimeZone, self.__DST, self.__continentState, 
                self.__hemisferio))
        
    # Redefinimos el método length. Le retornaremos el valor de 12 en base al número de atributos.
    def __len__(self):
        return 12
    
    # Getters y Setters a los atributos privados.
    def getId(self):
        return self.__id
    
    
    def setId(self, id):
        self.__id = id
        
    
    def getAirportName(self):
        return self.__airportName
    
    def setAirportName(self, AirportName):
        self.__airportName = AirportName
        
    
    def getCity(self):
        return self.__city
    
    def setCity(self,city):
        self.__city = city
        
    
    def getCountry(self):
        return self.__country
    
    def setCountry(self,country):
        self.__country = country
        
    
    def getIATACode(self):
        return self.__IATACode
    
    def setIATACode(self,IATACode):
        self.__IATACode = IATACode
        
    
    def getICAOCode(self):
        return self.__ICAOCode
    
    def setICAOCode(self,ICAOCode):
        self.__ICAOCode = ICAOCode
        
    
    def getLatitude(self):
        return self.__latitude
    
    def setLatitude(self,latitude):
        self.__latitude = latitude
        
    
    def getLongitude(self):
        return self.__longitude
    
    def setLongitude(self,longitude):
        self.__longitude = longitude
        
    
    def getAltitude(self):
        return self.__altitude
    
    def setAltitude(self,altitude):
        self.__altitude = altitude
        
    
    def getUTCTimeZone(self):
        return self.__UTCTimeZone
    
    def setUTCTimeZone(self,UTCTimeZone):
        self.__UTCTimeZone = UTCTimeZone
        
    
    def getDST(self):
        return self.__DST
    
    def setDST(self,DST):
        self.__DST = DST
        
    
    def getContinentState(self):
        return self.__continentState
    
    def setContinentState(self,continentState):
        self.__continentState = continentState
        
    
    def getHemisferio(self):
        return self.__hemisferio
    
    # No sería normal que le podamos envíar el emisferio ya que este se genera en automático
    # Así que solo lo dejo mencionado.
    # def set(self,):
    #     self.__hemisferio = "Hemisferio Norte" if float(self.__latitude)>0 else "Hemisferio Sur"

    
    def getNativeName(self):
        return self.__nativeName
    
    def setNativeName(self,nativeName):
        self.__nativeName = nativeName