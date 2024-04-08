# Diseño
![alt text](imgs/image-3.png)
# Instalación
```bash
git clone https://github.com/luisEmilioG1/proy-analisis

cd proy-analisis

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
python3 -m unittest entrega1.py
```