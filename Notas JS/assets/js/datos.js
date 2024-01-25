function ingresarNotas() {

    // html notas
    const htmlNota1 = parseFloat(prompt("Ingrese Nota 1 [HTML]"))
    document.querySelector('#htmlNota1').innerHTML = htmlNota1

    const htmlNota2 = parseFloat(prompt("Ingrese Nota 2 [HTML]"))
    document.querySelector('#htmlNota2').innerHTML = htmlNota2

    const htmlNota3 = parseFloat(prompt("Ingrese Nota 3 [HTML]"))
    document.querySelector('#htmlNota3').innerHTML = htmlNota3

    // css notas

    const cssNota1 = parseFloat(prompt("Ingrese Nota 1 [CSS]"))
    document.querySelector('#cssNota1').innerHTML = cssNota1

    const cssNota2 = parseFloat(prompt("Ingrese Nota 2 [CSS]"))
    document.querySelector('#cssNota2').innerHTML = cssNota2

    const cssNota3 = parseFloat(prompt("Ingrese Nota 3 [CSS]"))
    document.querySelector('#cssNota3').innerHTML = cssNota3

    // js notas

    const jsNota1 = parseFloat(prompt("Ingrese Nota 1 [JavaScript]"))
    document.querySelector('#jsNota1').innerHTML = jsNota1

    const jsNota2 = parseFloat(prompt("Ingrese Nota 2 [JavaScript]"))
    document.querySelector('#jsNota2').innerHTML = jsNota2

    const jsNota3 = parseFloat(prompt("Ingrese Nota 3 [JavaScript]"))
    document.querySelector('#jsNota3').innerHTML = jsNota3

    htmlPromedio = (htmlNota1 + htmlNota2 + htmlNota3) / 3;

    cssPromedio = (cssNota1 + cssNota2 + cssNota3) / 3;

    jsPromedio = (jsNota1 + jsNota2 + jsNota3) / 3;

    console.log(htmlPromedio);
    console.log(cssPromedio);
    console.log(jsPromedio);

    document.querySelector('#htmlPromedio').innerHTML = htmlPromedio
    document.querySelector('#cssPromedio').innerHTML = cssPromedio
    document.querySelector('#jsPromedio').innerHTML = jsPromedio
}
