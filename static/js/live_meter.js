let value = 0;

let target = 94;

let interval = setInterval(() => {

    value++;

    document.getElementById("meter-value").innerHTML = value + "%";

    if(value >= target){
        clearInterval(interval);
    }

}, 20);