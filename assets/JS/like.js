function like(id){
    var element = document.getElementById("like")
    var count = document.getElementById("count")
    $.get(`/articles/article_like/${id}`).then(response =>{
        if(response['response'] === "unliked"){
            element.className = "bx bx-heart h5 px-4 like"
            count.innerText = Number(count.innerText) - 1
        }
        else{
            element.className = "bx bxs-heart h5 px-4 red"
            count.innerText = Number(count.innerText) + 1
        }
    })
}