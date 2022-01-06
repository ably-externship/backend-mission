function makeQuestion(){
        $.ajax({
            type:"POST",
            url:"qna", //shop/shopid
            data:{title_give: $('#title').val() ,user_give:$('#user').val(), qna_give:$('#question').val()},
            success : function(response){
                //alert(response);
                window.location.reload();
            }
        })
        }