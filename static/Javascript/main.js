const input = document.getElementsByClassName('range');
const output = document.getElementsByClassName('output');
const setting = document.getElementsByClassName('setting');
const options = document.getElementsByClassName('option');
const result_btn = document.getElementById('button');
const result = document.getElementById('result');
const note = document.getElementById('note');

for (let i = 0; i < setting.length; i++) {
     setting.item(i).addEventListener('click', function () {
          for (let j = 0; j < setting.item(i).childNodes.length; j++) {
               if(setting.item(i).childNodes[j].className == 'main-body'){
                    setting.item(i).childNodes[j].style.display = 'block'
               }else if (setting.item(i).childNodes[j].className == 'fa fa-caret-down'){
                    setting.item(i).childNodes[j].className = ''
               }
          }
     })
}

result_btn.onclick = function () {
     this.style.display = 'none'
     document.getElementById('result-container').style.display = 'block'
}
result.onclick = function () {
     let result_text = result.innerText
     result_text = result_text.replace('Click To Copy Css', '')
     
     navigator.clipboard.writeText(result_text);
     setInterval(() => {
          note.innerText = 'Click To Copy Css'
     }, 5000);
     note.innerText = '🎉🎉 Css Copied 🎉🎉'
     
}     