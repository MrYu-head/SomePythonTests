// ajax将username和password发送到后端app_server.py进行验证
function submit(){
    $.ajax({
        url : "/login",
        type : "post",
        dataType : "json",
        // JSON.strinfify()转换数据为json格式
        // data : JSON.stringify({
        //     username : $("#username_text").val(),
        //     password : $("passNum").val()
        // }),
        data : {
            username : $("#username_text").val(),
            password : $("passNum").val()
        },
        success : function(data){
            alert('登陆成功。')
            console.log(data)
            console.log(data.status)
        },
        error : function(){
            // alert('登陆失败')
            console.log('**********');
        }
    })    
}
