## Titulo de la aplicacion  
*"FinanzasFit"*  

## Documento de la definicion del problema
### *Definición del problema.*  
Este problema a desarrollar los observamos cuando las personas tienen problemas al querer llevar un control de gastos, ya que es tedioso ver mucho número y tener que estar sumando o restando manualmente llega a molestar a las personas, 
Esta aplicación a desarrollar tiene como propósito ofrecer al usuario una herramienta que le permitirá llevar un manejo de sus gastos y ahorros de manera digital, con esto buscando que el usuario no tenga problemas sobre un mal manejo de dinero como gasto de mas cuando el producto vale menos, o no poder tener una división para que es cada parte de su dinero.
### *Alcance de la aplicación*
¿Que alcance tiene esa aplicación? Para nosotros el desarrollo de esta aplicación tiene alcances inimaginables, podría haber funciones que agregar que sean de mucha utilidad ya sea en diseño o algo que facilite al usuario el uso, que aun no llegamos a pensar (siempre y cuando este en nuestro conocimiento saber cómo se hace:)) además de que la información del usuario siempre estará segura mediante el registro y el inicio de sesión, tendrán un seguimiento de ahorros y de gastos, esa es la idea principal del proyecto.
### *Entidades.*
Hemos detectado 3 entidades que son las que nos ayudaran a manejar este proyecto de forma correcta y entendible, una de las entidades es **Usuario** esta es la entidad mas importante, ya que es el pilar sistema, sin esta no habrá mas entidades, en esta entidad tenemos, id_usuario (llave primaria) con esta se va a identificar a cada usuario, también tenemos, el email y el password, el nombre del usuario es importante, también esta la fecha del registro y su último acceso además de la foto del usuario, otra entidad es **dinero**, representa el estado financiero de justamente el usuario vinculada por medio del id_usuario ya que usuario tiene presupuesto pero también con sus campos de id_dinero y presupuesto, la siguiente entidad es **gastos**, como su nombre lo indica esta parte es sobre los gasto que tendrá el usuario de su presupuesto, esta contiene el id_gasto, titulo, descripción del gasto, el tipo de gasto y su gasto aproximado, de la manera en la que se relacionan con las otras tablas es por medio del id_usuario, ya que registra gasto y con la entidad dinero se relación por medio de id_dinero ya que gasto usa dinero tablas es por medio del id_usuario, ya que registra gasto y con la entidad dinero se relación por medio de id_dinero ya que gasto usa dinero

### Diagrama ER.  
<img width="400" height="450" alt="Diagrama ER" src="https://github.com/user-attachments/assets/4f3ea4eb-b5e4-4a1e-93b6-a10a003f0b68" />

## Integrantes

- **Romo Alvarado Luis Angel**
  - Correo Electronico:23308060610320@cetis61.edu.mx
  - Edad: 17
  - Especialidad: Programacion
  - Instituto: CETis61
  ### Fotografia
  - ![Luis](https://github.com/user-attachments/assets/0308d6a8-3024-47be-b6bf-f39205529a93)  


- **Sagarnaga Macias Jesus Antonio**  
  - Correo Electronico:23308060610320@cetis61.edu.mx
  - Edad: 17
  - Especialida: Programacion
  - Instituto: CETis61
  ### Fotografia
  ![Jesus](https://github.com/user-attachments/assets/dc2dd459-24ba-47ae-9494-5b4a5bf3f60b)

