const comment = document.getElementById('body')
const comment_btn = document.getElementById('btns')

document.getElementById('cancel-btn').onclick = function () {
     
     let fields = document.getElementsByClassName('comment-sec')
     for (var i = 0; i < fields.length; i++) {
          fields.item(i).value = ''
     }
}

comment.onclick = function(){
     comment_btn.style.display = 'block'
}
