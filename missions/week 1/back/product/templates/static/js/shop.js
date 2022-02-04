function findItem(){
    $.ajax({
        type:"POST",
        url:"/item/search",
        data:{item_search: $('#item').val() },
        success : function(response){
            alert(response["msg"]);
            window.location.reload();
        }
    });
}


$(document).ready(function(){
    $('#cards-box').empty();
    //listing();
    //showArticles();
});

function showArticles(){
    $.ajax({
        type: "GET",
        url: "/memo-link/v2",
        data: {},
        success : function (response){
            alert(response['msg']);
            let articles = response['articles'];
            for (let i =0;i<articles.length;i++){
                let title  = articles[i]['title'];
                let desc = articles[i]['desc'];
                let image = articles[i]['image'];
                let comment = articles[i]['comment'];
                console.log(title);
                let temp_html = `<div className="card">
                                                 <img className="card-img-top" src=${image} alt="Card image cap">
                                                 <div className="card-body">
                                                     <p className="card-text comment">${comment}</p>
                
                                                     <h5 href="${url}" className="card-title">${title}</h5>
                                                     <p className="card-text">${desc}</p>
                                                     <a href="#" class="btn btn-primary">Go somewhere</a>
                
                                                 </div>
                                             </div>`

                $('#cards-box').append(temp_html);
            }
        }
    })
}
