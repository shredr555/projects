var api_key = 'sAodYDumyn8RKQKEm74cfUiL44wto4wh'
var url = `https://api.giphy.com/v1/gifs/trending?api_key=${api_key}`

var grid = document.querySelector('.grid')

var imgs = []
var a = 10

var create = function (url) {
    fetch(url).then(response => response.json())
    .then(content => {
        for (var i=0; i < 10; i++) {
            let img = document.createElement('img')
            img.classList.add('element')
            img.src = content.data[i].images.downsized.url
            grid.appendChild(img)
            imgs.push(img)
        }
        more.onclick = function () {
            for (var i=a; i < a+5; i++) {
                let img = document.createElement('img')
                img.classList.add('element')
                img.src = content.data[i].images.downsized.url
                grid.appendChild(img)
                imgs.push(img)
            }
            a = a + 5
        }
    })
}

create(url)

btn.onclick = function () {
    for (var i=0; i < imgs.length; i++) {
        imgs[i].parentNode.removeChild(imgs[i])
    }
    imgs.splice(0, imgs.length)
    var search = document.querySelector('.search').value
    if (search == '') {
        url = `https://api.giphy.com/v1/gifs/trending?api_key=${api_key}`
        create(url)
    } else {
        url = `https://api.giphy.com/v1/gifs/search?api_key=${api_key}&q=${search}`
        create(url)
    }
}