const btndangky = document.getElementById("dangky");
const Quaylai = document.getElementById("quaylai");

const mainform = document.querySelector(".total_form");
btndangky.addEventListener('click',()=>{
    mainform.classList.toggle('active');
});
Quaylai.addEventListener('click',()=>{
    mainform.classList.toggle('active');
});


const filechooser = document.getElementById("filechooser");
const btn__chonanh = document.getElementById("btn__chonanh");
const anh_choosed = document.getElementById("anh_choosed");
btn__chonanh.addEventListener("click",function(){
    filechooser.click();
});
filechooser.addEventListener("change",()=>{
    if(filechooser.value){
        btn__chonanh.innerHTML = filechooser.value.match(/[\/\\]([\w\d\s\.\-\(\)]+)$/)[1];
        anh_choosed.src = URL.createObjectURL(filechooser.files[0]);
    }
});

const show_password = document.getElementById("show_password");
const input_text_form = document.getElementById("input_password");
show_password.addEventListener('click',()=>{
    show_password.classList.toggle('fa-eye');
    const type = input_text_form.getAttribute('type') === 'password'? 'text': "password";
    input_text_form.setAttribute('type',type);
});

const show_password1 = document.getElementById("show_password1");
const mklogin = document.getElementById("inputmklogin");
show_password1.addEventListener('click',()=>{
    show_password1.classList.toggle('fa-eye');
    const type = mklogin.getAttribute('type') === 'password'? 'text': "password";
    mklogin.setAttribute('type',type);
});

const inputText = document.getElementById("hide_close_name");
const clearIcon = document.getElementById("xoa");

inputText.addEventListener('input', () => {
  const value = inputText.value;
  clearIcon.style.display = value !== '' ? 'block' : 'none';
});

clearIcon.addEventListener('click', () => {
  inputText.value = '';
  clearIcon.style.display = 'none';
});

const ten = document.getElementById("ten");
const xoa1 = document.getElementById("xoa1");

ten.addEventListener('input', () => {
  const value = ten.value;
  xoa1.style.display = value !== '' ? 'block' : 'none';
});

xoa1.addEventListener('click', () => {
    ten.value = '';
    xoa1.style.display = 'none';
});


const email = document.getElementById("email");
const xoa2 = document.getElementById("xoa2");

email.addEventListener('input', () => {
  const value = email.value;
  xoa2.style.display = value !== '' ? 'block' : 'none';
});

xoa2.addEventListener('click', () => {
    email.value = '';
    xoa2.style.display = 'none';
});

const inputtk = document.getElementById("inputtk");
const xoa3 = document.getElementById("xoa3");

inputtk.addEventListener('input', () => {
  const value = inputtk.value;
  xoa3.style.display = value !== '' ? 'block' : 'none';
});

xoa3.addEventListener('click', () => {
    inputtk.value = '';
    xoa3.style.display = 'none';
});