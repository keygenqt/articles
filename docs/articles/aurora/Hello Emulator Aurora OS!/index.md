# Hello Emulator Aurora OS!

Все мобильные платформы стараются предоставить максимально удобные инструменты для разработки под них.
Один из таких инструментов - эмулятор, программа, которая имитирует образ и копирует функционал операционной системы.
Некоторые симулируют, но это уже другая история.

Работа с эмулятором зачастую проста - запустил из IDE, посмотрел, что все работает, проверил для надежности на девайсе.
Но бывают случаи когда с ним приходится поработать поплотнее: поставить недостающий пакет, закинуть файлы, посмотреть логи запущенных программ.
Не весь функционал, какой бы он ни был крутой, может покрыть GUI.
Вот терминал с доступом по ssh никто не превзойдет.

### Установка

Все ниже изложенное было выполнено на Windows, но работать будет примерно так же и на других операционных системах.
Так как мы говорим об эмуляторе, думаю Aurora SDK уже у вас стоит.
Если нет, вы всегда можете ее скачать и поставить [Аврора SDK](https://community.omprussia.ru/documentation/software_development/sdk/downloads.html).
Предварительно поставьте [VirtualBox](https://www.virtualbox.org/wiki/Downloads), именно там будет крутиться, и радовать нас, эмулятор.
Есть вариант с Docker, если вам скучно, то почему бы и нет.

На Windows мы любим окошечки.
Поставим [FileZilla](https://filezilla-project.org/download.php), через нее мы сможем закинуть файлы на эмулятор.

<p>
  <img src="https://api.keygenqt.com/api/ps/file/33e42f8a-553b-404c-b3bd-d95317b14a96.png"/>
</p>

Но без терминала не обойтись, чтобы не сломать себе мозг, поставим [WSL](https://ubuntu.com/wsl), через него мы легко попадем на эмулятор.

<p>
  <img src="https://api.keygenqt.com/api/ps/file/bb52400f-d1e0-4f58-8155-810bd7cf74b4.png"/>
</p>

### Запуск

Запустить эмулятор можно из IDE, а можно из VirtualBox просто как обычную виртуальную машину.
Еще VirtualBox имеет CLI интерфейс, запустить можно из терминала, если очень хочется.
В VirtualBox будет стоять еще `Aurora Build Engine` - вот это не эмулятор, кликать надо на ту где есть Aurora OS в названии.

<p>
  <img src="https://api.keygenqt.com/api/ps/file/ff956a3d-79ea-4da8-a1d2-fcce3f4cdd6a.png"/>
</p>

### SSH

Итак, нам нужно попасть в командную строку эмулятора по своим делам.
Мы можем зайти под дефаултным пользователем defaultuser и под юзером root, все зависит от целей.
Ключи ssh лежат `$HOME_SDK/vmshare/ssh/private_keys/sdk`.
Из под WSL этот путь будет такой: `/mnt/c/AuroraOS/vmshare/ssh/private_keys/sdk`.
Порт эмулятора `2223`, хост - `localhost`.
И так вся информация для входа у нас есть, можно выполнять команду в терминале WSL.

User: **defaultuser**

```shell
ssh -i /mnt/c/AuroraOS/vmshare/ssh/private_keys/sdk -p 2223 defaultuser@localhost
```

<p>
  <img src="https://api.keygenqt.com/api/ps/file/cdfe747e-0f21-4042-b79f-e31f227dedbc.png"/>
</p>

User: **root**

```shell
ssh -i /mnt/c/AuroraOS/vmshare/ssh/private_keys/sdk -p 2223 root@localhost
```

<p>
  <img src="https://api.keygenqt.com/api/ps/file/5903958b-3df3-4601-a469-118dd2e9c05f.png"/>
</p>

### Передача данных на эмулятор

Так как у нас есть доступ по ssh мы можем воспользоваться CLI приложением `scp`, которое без проблем предаст ваши файлы на эмулятор.
Выглядеть команда будет примерно так:

```shell
scp -i /mnt/c/AuroraOS/vmshare/ssh/private_keys/sdk -P 2223 /path/to/img.png defaultuser@localhost:/home/defaultuser/Downloads
```

Но мы любим окошечки, писать эту жуткую команду не в нашем стиле.
Мы просто настроим FileZilla и работать с файлами станет сильно удобней.
В первую очередь добавим наш ключ в настройках SFTP.

<p>
  <img src="https://api.keygenqt.com/api/ps/file/256d153b-86b4-42e3-b2ea-95b1c1d27778.png"/>
</p>

Теперь можно добавить SFTP сервер.

* Protocol: SFTP
* Host: localhost
* Port: 2223
* Login Type: Normal (пароль спрашивать не будет, оставляем пустым)
* User: defaultuser

<p>
  <img src="https://api.keygenqt.com/api/ps/file/49afe5c0-5905-4acc-8458-bc55c86983f5.png"/>
</p>

Ну вот и все. Теперь можно жать Connect и вся файловая система доступная пользователю `defaultuser` перед вами.

<p>
  <img src="https://api.keygenqt.com/api/ps/file/c331d8c3-7cc2-499b-a445-9ad691f3e980.png"/>
</p>

### Где девайс?

Эмулятор - это хорошо, вот бы телефон где-нибудь намутить?
А я вам скажу: "Жаль, но его не купить, пока что, но есть вариант - присоединяйтесь к программе [Бета-Тестирования](https://auroraos.ru/beta)."

Удачи!