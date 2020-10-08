const slides = document.querySelector(".slider").children;

const prev = document.querySelector(".prev");
const next = document.querySelector(".next");
let index = 0;
const indicator = document.querySelector(".indicator");

prev.addEventListener("click", function(){
    prevSlide();
    updateCircleIndicator();
    resetTimer();
})

next.addEventListener("click", function(){
    nextSlide();
    updateCircleIndicator();
    resetTimer();
})

function circleIndicator(){
    for(let i = 0; i < slides.length; i++){
        const div = document.createElement("div");
            div.innerHTML;
            div.id = i;
        div.setAttribute("onclick", "indicateSlide(this)");
        if(i===0){
            div.className = "activ";
        }
        indicator.appendChild(div);
    }

}

circleIndicator();

function indicateSlide(element){
    index = element.id;
    changeSlide();
    updateCircleIndicator();
    resetTimer();
}

function updateCircleIndicator(){
    for(let i = 0; i < indicator.children.length; i++){
        indicator.children[i].classList.remove("activ");
    }
    indicator.children[index].classList.add("activ");
}

function prevSlide() {
    if (index === 0) {
        index = slides.length - 1;
    } else {
        index--;
    }
    changeSlide();
}

function nextSlide(){
    if(index === slides.length - 1){
        index = 0;
    }
    else{
        index++;
    }
    changeSlide();
}

function changeSlide(){
    for(let i = 0; i < slides.length; i++){
        slides[i].classList.remove("activ");
    }


    slides[index].classList.add("activ");
}

function resetTimer(){
    clearInterval(timer);
    timer = setInterval(autoPlay, 8000);
}

function autoPlay(){
    nextSlide();
    updateCircleIndicator();
}

let timer = setInterval(autoPlay, 8000);