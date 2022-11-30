
function agregarProducto()
{
    let nombreProducto = document.getElementById('nombreProducto')
    let estadoProducto = document.getElementById('estadoProducto')
    let precioProducto = document.getElementById('precioProducto')
    let cantidadProducto = document.getElementById('cantidadProducto')

    let cuerpoTabla = document.getElementById('cuerpoTabla')

    cuerpoTabla.innerHTML += `
    <tr>
        <td>${nombreProducto.value}</td>
        <td>${cantidadProducto.value}</td>
        <td>${estadoProducto.value}</td>
        <td>${precioProducto.value}</td>
    </tr>
    `
}

addEventListener('DOMContentLoaded', ()=>{
    let infoProducto = document.getElementById('infoProducto')

    infoProducto.onchange = function()
    {
        identificador = infoProducto.value
        fetch(`http://127.0.0.1:8000/proyCurso/obtenerInfo?producto=${identificador}`)
        .then(response => response.json())
        .then(data => {
            console.log(data)
            let nombreProducto = document.getElementById('nombreProducto')
            let estadoProducto = document.getElementById('estadoProducto')
            let precioProducto = document.getElementById('precioProducto')

            nombreProducto.value = data.dato[0]
            estadoProducto.value = data.dato[3]
            precioProducto.value = data.dato[1]

        })
    }
})