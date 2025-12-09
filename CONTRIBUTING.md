# Guía de Contribución

Esta guía explica cómo organizar y agregar soluciones al repositorio de Advent of Code.

## Estructura de Archivos

Para cada día del desafío, crea un directorio siguiendo esta estructura:

```
YYYY/
└── dayXX/
    ├── README.md           # Descripción del problema y solución
    ├── solution.*          # Tu solución (ej: solution.py, solution.js, etc.)
    ├── input.txt           # Tu entrada personal del problema
    └── test_input.txt      # (Opcional) Entrada de ejemplo del problema
```

## Añadir una Nueva Solución

1. **Crear el directorio del día:**
   ```bash
   mkdir -p YYYY/dayXX
   ```

2. **Copiar la plantilla README:**
   - Usa el README de ejemplo en `2024/day01/README.md` como plantilla
   - Actualiza el número del día y el enlace al problema

3. **Agregar tu solución:**
   - Nombra tu archivo de solución claramente (ej: `solution.py`, `solution.js`)
   - Incluye comentarios explicativos en el código
   - Asegúrate de que el código sea limpio y legible

4. **Agregar archivos de entrada:**
   - Guarda tu entrada personal en `input.txt`
   - Si lo deseas, incluye el ejemplo de entrada en `test_input.txt`

5. **Documentar tu solución:**
   - Describe tu enfoque en el README
   - Incluye la complejidad temporal y espacial
   - Agrega instrucciones de ejecución
   - Anota cualquier desafío interesante o aprendizaje

6. **Actualizar el progreso:**
   - Marca el día como completado en `YYYY/README.md`
   - Actualiza la tabla de progreso en el README principal

## Mejores Prácticas

### Código

- ✅ Escribe código limpio y legible
- ✅ Usa nombres descriptivos para variables y funciones
- ✅ Agrega comentarios para lógica compleja
- ✅ Considera la eficiencia algorítmica
- ✅ Maneja casos borde apropiadamente

### Documentación

- ✅ Explica tu enfoque de solución
- ✅ Documenta la complejidad del algoritmo
- ✅ Incluye instrucciones de ejecución
- ✅ Comparte aprendizajes o desafíos interesantes

### Organización

- ✅ Mantén un directorio por día
- ✅ Sigue la estructura de nombrado consistente
- ✅ Actualiza el progreso en los READMEs

## Ejemplo de README para un Día

```markdown
# Día X: Título del Problema

[Link al problema](https://adventofcode.com/YYYY/day/X)

## Descripción del Problema

### Parte 1
Breve descripción de lo que hay que resolver.

### Parte 2
Breve descripción de la segunda parte.

## Solución

### Enfoque
Explicación de tu estrategia para resolver el problema.

### Complejidad
- **Tiempo:** O(n log n)
- **Espacio:** O(n)

## Ejecución

\`\`\`bash
python solution.py
\`\`\`

## Notas
Cualquier observación interesante, optimizaciones aplicadas, o desafíos encontrados.
```

## Lenguajes de Programación

Puedes usar cualquier lenguaje de programación que prefieras. Algunos ejemplos:

- Python: `solution.py`
- JavaScript: `solution.js`
- Java: `Solution.java`
- C++: `solution.cpp`
- Go: `solution.go`
- Rust: `solution.rs`

## Privacidad

⚠️ **Importante:** No compartas tu entrada personal (`input.txt`) públicamente si el repositorio es público, ya que Advent of Code solicita mantener las entradas privadas. Puedes usar `.gitignore` para excluir estos archivos.

Para excluir entradas:
```bash
echo "**/input.txt" >> .gitignore
```

## Preguntas

Si tienes preguntas sobre cómo organizar tus soluciones, consulta los ejemplos existentes en el repositorio o revisa la documentación oficial de Advent of Code.

---

¡Feliz programación y buena suerte con los desafíos! 🎄✨
