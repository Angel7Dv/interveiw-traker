const $ =(obj)=> document.querySelector(obj)

function showing(obje){
    const div = $(obje)
    div.classList.toggle("hidden")

}