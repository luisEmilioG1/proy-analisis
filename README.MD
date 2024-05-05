# Diseño
![alt text](imgs/image-3.png)

# Instalación
```bash
git clone https://github.com/luisEmilioG1/proy-analisis
cd proy-analisis
```

# Versiones
PS C:\Users\luise> python --version
Python 3.11.5

PS C:\Users\luise> pip --version
pip 23.2.1 from C:\Python311\Lib\site-packages\pip (python 3.11)

### Windows
```bash
python -m venv myenv
myenv\Scripts\activate

pip install -r requirements.txt
```

# Entrega 1
Se permite calcular la distribución de probabilidades de cualquier subsistema de estados no vacíos `(current_state | next_state = xxxx)` partiendo de tablas `EstadoCanalF`
![alt text](imgs/image.png)

### test 1
`(ABC | AC=10 )` 
![alt text](imgs/image-1.png)
### test 2
`(ABC | ABC=110)`
![alt text](imgs/image-2.png)

## Ejecución
```bash
python -m unittest entrega1.py
```

# Entrega 2
## Diseño
![alt text](imgs/desing2.png)

## Características
* Cálculo de distribuciones de probabilidades con vacío tanto en presente como en futuro
* Crear un grafo que representa un sistema dado por (f_state|c_state=XXXX)
* Eliminación y restablecimiento de cualquier conección del grafo  
* Verificar distancia entre distribuciones de probabilidad

## Ejecución
```bash
python entrega2.py
```