/*-----------------------CREATING TABLES---------------------*/ 

CREATE TABLE city ( 

CityName varchar (50) not null primary key, 

Country varchar2(50) 

); 

  

create table Airport ( 

AirPortName VARCHAR2(50) not null primary key, 

Countary varchar2(50), 

CityName varchar(50)  not null  

); 

Create table have ( 

AirPortName VARCHAR2(50) not null , 

AirlineID VARCHAR2(50) not null 

); 

create table Airline( 

OfficeID number unique not null , 

ThreeDigitCode number unique not null, 

AirlineID VARCHAR2(50) primary key not null, 

AirlineName varchar2(50) unique  

); 

Create table Flight ( 

Source VARCHAR2(50) NOT NULL, 

FlightCode VARCHAR2(6)NOT NULL primary key, 

Destination VARCHAR2(50) NOT NULL, 

Duration VARCHAR2(50) , 

DepartureT VARCHAR2(50) NOT NULL, 

ArrivelTime VARCHAR2(50) NOT NULL, 

AirlineID VARCHAR2(50)  not null, 

EmployeeID number NOT NULL 

); 

  

create table Passenger ( 

Sex VARCHAR2(20), 

Lname VARCHAR2(50) NOT NULL, 

Fname VARCHAR2(50) NOT NULL, 

Age date, 

PID number  NOT NULL Primary Key,  

PassportNumber  VARCHAR2(7)NOT NULL, 

PPhone NUMBER, 

FlightCode VARCHAR2(6)NOT NULL 

); 

create table Ticket ( 

TicketNumber VARCHAR2(13) Primary Key, 

DateOfTravel DATE  NOT NULL, 

ArrivelTime VARCHAR2(50) NOT NULL,  

DepartureT  VARCHAR2(50) NOT NULL, 

SeatNumber VARCHAR2(3) UNIQUE,    

Source VARCHAR2(50), 

Destination VARCHAR2(50), 

PID number  NOT NULL, 

EmployeeID number  NOT NULL 

); 

  

  

create table Employee ( 

Salary NUMBER, 

Lname VARCHAR2(50) NOT NULL, 

JobType VARCHAR2(50) NOT NULL, 

Fname VARCHAR2(50) NOT NULL, 

Age date , 

AirPortName VARCHAR2(50) not null , 

EmployeeID number Primary Key NOT NULL, 

Sex VARCHAR2(20), 

EPhone NUMBER, 

Password VARCHAR2(20) NOT NULL 

); 

  

Create table Serves( 

EmployeeID number NOT NULL, 

PID number not null 

);  

  

create table Books ( 

DateOfBooking DATE primary key, 

TicketNumber VARCHAR2(13), 

PID number  NOT NULL 

); 

  

create table Cancels ( 

DateOfCanselletion DATE primary key, 

TicketNumber VARCHAR2(13), 

PID number  NOT NULL 

); 

/*-----------------------END OF CREATING TABLES---------------------*/ 

/*-----------------------CONSTRAINTS---------------------*/ 

Alter table Airport  

add constraint Aitport_FK1 FOREIGN KEY (CityName) REFERENCES  city(CityName); 

  

Alter table have  

add constraint have_FK1 FOREIGN KEY (AirPortName) REFERENCES Airport(AirPortName); 

  

Alter table have  

add constraint have_FK2 FOREIGN KEY (AirlineID) REFERENCES Airline(AirlineID); 

  

Alter table Airline  

add constraint CHECK_length_1 CHECK (length (OfficeID) =4  and length(ThreeDigitCode)=3 ) ; 

  

Alter table Flight  

add constraint CHECK_length_2 CHECK (length(FlightCode) <6 or length(FlightCode) =6  ); 

  

Alter table Flight  

add constraint Flight_FK1 FOREIGN KEY (AirlineID) REFERENCES  Airline(AirlineID); 

  

Alter table Flight  

add constraint Flight_FK2 FOREIGN KEY (EmployeeID) REFERENCES  Employee(EmployeeID); 

  

Alter table Passenger  

add constraint Passenger_FK1 FOREIGN KEY (FlightCode) REFERENCES Flight (FlightCode); 

  

Alter table Passenger  

add constraint CHECK_length_3 CHECK ( length(PassportNumber) =7 and length(PPhone)=8 and length(PID) =10); 

  

Alter table Ticket  

add constraint CHECK_length_4 CHECK (length(PID) =10); 

  

Alter table Ticket  

add constraint Ticket_FK1 FOREIGN KEY (PID) REFERENCES  Passenger(PID); 

  

Alter table Ticket 

add constraint ticket_FK2  FOREIGN KEY(EmployeeID) references employee(EmployeeID); 

  

Alter table Serves  

add constraint Serves_FK1 FOREIGN KEY (employeeID) REFERENCES  employee(employeeID); 

  

Alter table Serves 

add Constraint  serves_FK2 FOREIGN KEY (PID ) references Passenger(PID)  ; 

  

Alter table Employee 

add constraint CHECK_length_5 CHECK ( length(EPhone)=8 and length(EmployeeID)=10) ; 

  

Alter table Employee 

add constraint Employee_FK1 FOREIGN KEY (AirPortName) REFERENCES Airport(AirPortName); 

  

Alter table cancels 

add Constraint  cancels_FK1 FOREIGN KEY (TicketNumber ) references ticket(TicketNumber)  ; 

  

Alter table cancels 

add Constraint  cancels_FK2 FOREIGN KEY (PID ) references Passenger(PID)  ; 

  

Alter table books 

add Constraint  books_FK1 FOREIGN KEY (TicketNumber ) references ticket(TicketNumber)  ; 

  

Alter table books 

add Constraint  books_FK2 FOREIGN KEY (PID ) references Passenger(PID)  ; 

/*-----------------------END OF CONSTRAINTS---------------------*/ 

  

  

insert into city (CityName,country) values ('abha','saudi arabia'); 

insert into Airport (AirPortName,Countary,CityName ) values ('abha international airport','saudi arabia','abha'); 

insert into airline(OfficeID  ,ThreeDigitCode ,AirlineID ,AirlineName) values (1234,229,'KU','Kuwait Airways'); 
insert into airline(OfficeID  ,ThreeDigitCode ,AirlineID ,AirlineName) values (5643,265,'SP','SOLINAIR'); 
insert into airline(OfficeID  ,ThreeDigitCode ,AirlineID ,AirlineName) values (5896,199,'TU','Tunisair'); 
insert into airline(OfficeID  ,ThreeDigitCode ,AirlineID ,AirlineName) values (5986,235,'TK','Turkish Airlines'); 


insert into Employee (Salary, Lname,JobType,Fname,Age,AirPortName,EmployeeID,Sex,EPhone,Password) values(5000, 'Ahmad', 'manager','hassan', TO_DATE('1989/04/05','yyyy/mm/ dd'),'abha international airport', 2111585893, 'Male', 55446688,123456); 
insert into Employee (Salary, Lname,JobType,Fname,Age,AirPortName,EmployeeID,Sex,EPhone,Password) values(3000, 'abdullah', 'engineer','yaseen', TO_DATE('1998/08/05','yyyy/mm/ dd'),'abha international airport', 5643218795, 'Male', 48956325,123456); 
insert into Employee (Salary, Lname,JobType,Fname,Age,AirPortName,EmployeeID,Sex,EPhone,Password) values(200, 'baqer', 'worker','yosif', TO_DATE('1978/04/07','yyyy/mm/ dd'),'abha international airport', 2181156439, 'Male', 69854723,123456); 

INSERT INTO flight ( Source ,FlightCode ,Destination ,Duration,DepartureT,ArrivelTime ,AirlineID ,EmployeeID) values ('Kuwait','KU1005','Istanbul','3:40','9:00AM','12:40PM','KU', 2111585893); 

INSERT INTO flight ( Source ,FlightCode ,Destination ,Duration,DepartureT,ArrivelTime ,AirlineID ,EmployeeID) values ('Oman','SP4306','USA','16:34','7:00AM','11:34PM','SP', 2111585893); 

INSERT INTO flight ( Source ,FlightCode ,Destination ,Duration,DepartureT,ArrivelTime ,AirlineID ,EmployeeID) values ('Emirates','TU4987','Iran','2:00','10:00AM','12:00PM','TU', 2111585893); 

INSERT INTO flight ( Source ,FlightCode ,Destination ,Duration,DepartureT,ArrivelTime ,AirlineID ,EmployeeID) values ('saudi arabia','TU5556','Australia','14:14','11:00AM','1:00AM','TU', 2111585893); 

INSERT INTO flight ( Source ,FlightCode ,Destination ,Duration,DepartureT,ArrivelTime ,AirlineID ,EmployeeID) values ('Qatar','TK6566','Kuwait','1:25','1:00PM','2:25PM','TK', 2111585893); 

insert into passenger (Sex, Lname,Fname, Age,PassportNumber,PID,PPhone,FlightCode) values ('Male', 'khaled','mohammad', TO_DATE('1999/04/05','yyyy/mm/ dd'),1234567, 1234567899,69676161, 'KU1005'); 

insert into passenger (Sex, Lname,Fname, Age,PassportNumber,PID,PPhone,FlightCode) values ('Female', 'Mnar','Abdullah', TO_DATE('1945/11/06','yyyy/mm/ dd'),5643218, 9966553384,69583246, 'SP4306'); 

insert into passenger (Sex, Lname,Fname, Age,PassportNumber,PID,PPhone,FlightCode) values ('Male', 'khaled','Ahmad', TO_DATE('1999/04/05','yyyy/mm/ dd'),5632984, 4466330022,69532016, 'TU4987'); 

insert into passenger (Sex, Lname,Fname, Age,PassportNumber,PID,PPhone,FlightCode) values ('Male', 'Ali','Abbas', TO_DATE('1999/04/05','yyyy/mm/ dd'),5698331, 8796425349,69852314,'TU5556'); 

insert into passenger (Sex, Lname,Fname, Age,PassportNumber,PID,PPhone,FlightCode) values ('Male', 'Abdulgader','Jassem', TO_DATE('1999/04/05','yyyy/mm/ dd'),7744653, 8796528430,98651423, 'TK6566'); 

insert into Have (AirportName,AirlineID) values ('abha international airport','KU' ); 

insert into ticket (DateOfTravel, ArrivelTime, DepartureT, SeatNumber, Source,Destination,TicketNumber,EmployeeID, PID) values ( TO_DATE('2022/03/05','yyyy/mm/ dd'),'12:40PM','9:00AM', '25c','Kuwait','Istanbul','2291234567890', 2111585893, 1234567899 ); 

insert into serves (EmployeeID, PID) values ( 2111585893, 1234567899); 

insert into books (DateOfBooking, TicketNumber,PID) values (TO_DATE('2022/04/05','yyyy/mm/ dd'), '2291234567890',1234567899 ); 

insert into cancels (DateOfCanselletion,TicketNumber,PID) values (TO_DATE('2022/04/05','yyyy/mm/ dd'),'2291234567890',1234567899); 

/**
BEGIN 

   FOR cur_rec IN (SELECT object_name, object_type 

                   FROM user_objects 

                   WHERE object_type IN 

                             ('TABLE', 

                              'VIEW', 

                              'MATERIALIZED VIEW', 

                              'PACKAGE', 

                              'PROCEDURE', 

                              'FUNCTION', 

                              'SEQUENCE', 

                              'SYNONYM', 

                              'PACKAGE BODY' 

                             )) 

   LOOP 

      BEGIN 

         IF cur_rec.object_type = 'TABLE' 

         THEN 

            EXECUTE IMMEDIATE 'DROP ' 

                              || cur_rec.object_type 

                              || ' "' 

                              || cur_rec.object_name 

                              || '" CASCADE CONSTRAINTS'; 

         ELSE 

            EXECUTE IMMEDIATE 'DROP ' 

                              || cur_rec.object_type 

                              || ' "' 

                              || cur_rec.object_name 

                              || '"'; 

         END IF; 

      EXCEPTION 

         WHEN OTHERS 

         THEN 

            DBMS_OUTPUT.put_line ('FAILED: DROP ' 

                                  || cur_rec.object_type 

                                  || ' "' 

                                  || cur_rec.object_name 

                                  || '"' 

                                 ); 

      END; 

   END LOOP; 

   FOR cur_rec IN (SELECT *  

                   FROM all_synonyms  

                   WHERE table_owner IN (SELECT USER FROM dual)) 

   LOOP 

      BEGIN 

         EXECUTE IMMEDIATE 'DROP PUBLIC SYNONYM ' || cur_rec.synonym_name; 

      END; 

   END LOOP; 

END; 
**/