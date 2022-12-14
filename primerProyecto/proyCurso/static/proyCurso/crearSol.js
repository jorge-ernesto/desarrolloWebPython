function crearSolicitud()
{
    let cuerpoTabla = document.getElementById('cuerpoTabla')
    console.log(cuerpoTabla.rows)
    console.log(cuerpoTabla.rows.length)
    longitudTabla = cuerpoTabla.rows.length
    arregloProductos = []
    for(let i = 0; i < longitudTabla; i++)
    {
        productoDatos = cuerpoTabla.rows.item(i)
        let producto = [productoDatos.cells.item(0).innerHTML,productoDatos.cells.item(1).innerHTML,productoDatos.cells.item(2).innerHTML,productoDatos.cells.item(3).innerHTML]
        arregloProductos.push(producto)
    }
    console.log(arregloProductos)

    url = '/proyCurso/agregarSolicitud'
    infoProductos = {
        'productosCapturados':arregloProductos
    }

    fetch(url,{
        method:"POST",
        headers: {
            "X-Request-With": "XMLHttpRequest",
            "X-CSRFToken": getCookie("csrftoken"),
        },
        body:JSON.stringify(infoProductos)
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
    })
}

function getCookie(name)
{
    let cookieValue = null;
    if(document.cookie && document.cookie !== "")
    {
        const cookies = document.cookie.split(";")
        for(let i=0;i < cookies.length; i++)
        {
            const cookie = cookies[i].trim();
            if((cookie.substring(0,name.length + 1 )) === (name + '='))
            {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1))
                break;
            }
        }
    }
    return cookieValue;
}

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