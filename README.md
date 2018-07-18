# PI-PoioHQ
*Aprendiendo a hacer un bot de telegram, con python en una Raspberry Pi 3 B+*

------

- ### PoioHQ/PoioHQ

  En teoria, este es el archivo para que se ejecute al inicio el .sh ( /etc/init.d/ ) pero al parecer no funciona.
  Cuando este arreglado, no haria falta ejecutar el .sh manualmente, sino que se iniciaria automaticamente.
  Tambien configura los estados y comandos para que se comporte como un programa

  ```
  pi@host ~:PoioHQ start|stop|restart
  ```

- ### PoioHQ/PoioHQ.sh

  Archivo que ejecuta el proceso del bot, la idea es que se ponga como "cron" o se ejecute al inicio del sistema (en caso de que se reinicie)

- ### PoioHQ/PoioHQ_bot.py

  Es el archivo principal del bot, donde los comandos se configuran.

- ### PoioHQ/log.txt

  Log ... do'h!

- ### PoioHQ/pys

  La carpeta donde se ponen los archivos que controlan los sensores y accesorios para la seguridad o tareas que se requieran hacer.
  Son los que se ejecutan desde el bot, en PoioHQ_bot.py

  - ### PoioHQ/pys/pir.py

    Controla los sensores de movimiento





### 



