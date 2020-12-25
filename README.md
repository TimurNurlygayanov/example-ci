Пример бесплатного CI
---------------------
Этот репозиторий является примером базовой настройки
бесплатного CI для гитхаб репозитория.


Как это работает
----------------

Файл [./circleci/config.yml](./circleci/config.yml) содержит
описание настроек для бесплатного CI сервиса [CircleCI](https://circleci.com/).

При изменении кода в данном репозитории CircleCI скопирует
новый код к себе и запустит все тесты, результаты 
тестов влияют на то, будет ли новый код "одобрен"
(если тесты прошли) или же изменения будут "отвергнуты"
(если тесты не прошли).

Изменения, которые были одобрены, а так же проверены вручную,
принимаются в основную ветку репозитория.

При таком подходе мы проверяем каждое изменение нашего кода,
и в главной ветке репозитория у нас всегда хранится версия кода,
которая успешно проходит все тесты.


Как отправить новый код на проверку?
------------------------------------
Все новые изменения делаются в отдельных ветках (git branches),
и после того, как изменения будут приняты, они попадают в
главную ветку main.

Для того, чтобы сделать новую ветку,
нам нужно выполнить такие команды:

```bash
git branch my_new_branch
git checkout my_new_branch
```

После этого нам нужно внести изменения в код,
и, когда все будет готово, выполнить такие команды,
чтобы отправить эти изменения на проверку:

```bash
git add .
git commit -am "Added new tests for PetFriends REST API"
git push origin my_new_branch
```

Обратите внимание, что мы делаем git push в новую ветку с именем
"my_new_branch".

Теперь можно открыть репозиторий 
https://github.com/TimurNurlygayanov/example-ci и мы увидим
предложение сделать pull request (нажмите на эту кнопку)


После того, как pull request готов, Circle CI запустит наши 
тесты, и, пока тесты не прошли, мы можем видеть такой статус:
![Tests in progress](images/tests_in_progress.png)

Когда тесты прошли, статус изменяется:
![Tests passed](images/tests_passed.png)

Примеры
-------
Пример изменений, которые прошли CI проверку:


Пример изменений, которые не прошли CI проверку,
потому что там есть ошибка:

