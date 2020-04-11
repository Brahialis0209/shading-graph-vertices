# Instruction
This application allows you to draw graph traversal algorithms in width and depth.
## Requirements
- Python 3.6-...
- packages indicated in `requirements.txt`
## Install, run, uninstall
1. Create a copy of the repository: `https://gitlab.com/Brahialis0209/shading-graph-vertices.git`
2. Go to the project folder - cd [path to the directory in which the project lies]/shading-graph-vertices
3. Install the missing packages - pip install -r requirements.txt
4. Go to the src directory - cd src
4. Run the application - python main.py example
## Work with the application
- Open a config text document and enter your graph in the following format:
1. start_node (here you indicate the vertex from which the traverse begins, for example 1)
2. traversal (here is a workaround for example DFS)
3. In the next lines, specify the graph itself, in each line 2 values - the vertices of your edges, <br> or one value -
  if this vertex is not the beginning of a new edge.

### Example
start_node 1<br>
traversal DFS<br>
1 2<br>
1 3<br>
1 4<br>
2 5<br>
2 6<br>
3 7<br>
4<br>
5<br>
6<br>
7 8<br>
8<br>


# Instruction in Russian
Это приложение позволяет отрисовать алгоритмы обхода графа в ширину и глубину.
## Требования
- Python 3.6-...
- пакеты, указанные в `requirements.txt`
## Установка, запуск, удаление
1. Cоздать копию репозитория: `https://gitlab.com/Brahialis0209/shading-graph-vertices.git`
2. Перейти в папку проекта - cd [путь к директории в которой лежит проект]/shading-graph-vertices
3. Установить недостающие пакеты - pip install -r requirements.txt
4. Перейти в диреторию src - cd src
4. Запустить приложение - python main.py example
## Работа с приложением
- Откройте текстовый документ config и введите свой граф в следующем формате:
1. start_node (тут вы указываете ту вершину с которой начинается обход, например 1)
2. traversal (здесь способ обхода, например DFS)
3. В следующих строчках задаете сам граф, в каждой строчке по 2 значения - вершины ваших рёбер,<br> либо одно значение -
 если эта вершина не является началом нового ребра.

### Пример
start_node 1<br>
traversal DFS<br>
1 2<br>
1 3<br>
1 4<br>
2 5<br>
2 6<br>
3 7<br>
4<br>
5<br>
6<br>
7 8<br>
8<br>
