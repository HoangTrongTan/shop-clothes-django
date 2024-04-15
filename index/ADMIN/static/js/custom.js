var filechooser = document.getElementById("filechooser");
const btn__chonanh = document.getElementById("btn__chonanh");
const anh_choosed = document.getElementById("anh_choosed");


const anh_choosed__add = document.getElementById("anh_choosed_add");
const filechooser_add = document.getElementById("filechooser_add");
const btn__addanh = document.getElementById("btn__addanh");

btn__chonanh.addEventListener("click",function(){
    filechooser.click();
});
filechooser.addEventListener("change",()=>{
    setAnh(btn__chonanh,anh_choosed,filechooser);
});


btn__addanh.addEventListener("click",()=>{
    filechooser_add.click();
});
filechooser_add.addEventListener("change",()=>{
    setAnh(btn__addanh,anh_choosed__add,filechooser_add);
})

function setAnh(btn,img,input){
    if(input.value){
        console.log(input.value)
        btn.innerHTML = input.value.match(/[\/\\]([\w\d\s\.\-\(\)]+)$/)[1];
        img.src = URL.createObjectURL(input.files[0]);
    }
}


const register__redirect = document.getElementById("register__redirect");
register__redirect.addEventListener("click",()=>{
    console.log("vào r");
    classList.toggle('active')
});