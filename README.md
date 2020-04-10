# Instruction
This application allows you to draw graph traversal algorithms in width and depth.
## Requirements
- Python 3.6-...
- packages indicated in `requirements.txt`
## Install, run, uninstall
- create a copy of the repository: `https://gitlab.com/Brahialis0209/shading-graph-vertices.git`
- open folder `shading-graph-vertices` as project PyCharm and start `src/main.py` with parameters 'src\config'
either in the folder `shading-graph-vertices/src`, execute the command: `python main.py config`
## Work with the application
- Open a config text document and enter your graph in the following format:
1. start_node=(here you indicate the vertex from which the traverse begins, for example 1)
2. traversal=(here is a workaround for example DFS)
3. In the next lines, specify the graph itself, in each line 2 values - the vertices of your edges.

### Example
start_node=1<br>
traversal=DFS<br>
1 2<br>
1 3<br>
1 4<br>
2 5<br>
2 6<br>
3 7<br>
4 empty<br>
5 empty<br>
6 empty<br>
7 8<br>
8 empty<br>


# Instruction in Russian
Это приложение позволяет отрисовать алгоритмы обхода графа в ширину и глубину.
## Требования
- Python 3.6-...
- пакеты, указанные в `requirements.txt`
## Установка, запуск, удаление
- создайте копию репозитория: `https://gitlab.com/Brahialis0209/shading-graph-vertices.git`
- откройте папку `shading-graph-vertices` как проект PyCharm и запустите `src/main.py` с параметром 'src\config'
либо, находясь в папке `shading-graph-vertices/src`, исполните команду: `python main.py config`
## Работа с приложением
- Откройте текстовый документ config и введите свой граф в следующем формате:
1. start_node=(тут вы указываете ту вершину с которой начинается обход, например 1)
2. traversal=(здесь способ обхода, например DFS)
3. В следующих строчках задаете сам граф, в каждой строчке по 2 значения - вершины ваших рёбер.

### Пример
start_node=1<br>
traversal=DFS<br>
1 2<br>
1 3<br>
1 4<br>
2 5<br>
2 6<br>
3 7<br>
4 empty<br>
5 empty<br>
6 empty<br>
7 8<br>
8 empty<br>
