let chronometerDays = document.getElementById("chronometerDays");
let chronometerHours = document.getElementById("chronometerHours");
let chronometerMinutes = document.getElementById("chronometerMinutes");
let chronometerSeconds = document.getElementById("chronometerSeconds");

function countdownTimer(endDate) {
    let timer, days, hours, minutes, seconds;

    endDate = new Date(endDate).getTime();

    if (isNaN(endDate)) {
        return;
    }

    timer = setInterval(function() {
        let now = new Date().getTime();
        let timeRemaining = parseInt((endDate - now) / 1000);

        if (timeRemaining >= 0) {
            days = parseInt(timeRemaining / 86400);
            timeRemaining = (timeRemaining % 86400);

            hours = parseInt(timeRemaining / 3600);
            timeRemaining = (timeRemaining % 3600);

            minutes = parseInt(timeRemaining / 60);
            timeRemaining = (timeRemaining % 60);

            seconds = parseInt(timeRemaining);

            let lengthDays = days.toString().length;
            let sliceDays = lengthDays > 2 ? lengthDays * -1 : -2;

            chronometerDays.innerText = ("0" + days).slice(sliceDays);
            chronometerHours.innerText = ("0" + hours).slice(-2);
            chronometerMinutes.innerText = ("0" + minutes).slice(-2);
            chronometerSeconds.innerText = ("0" + seconds).slice(-2);
        } else {
            return;
        }
    }, 1000);
}

let endDate = "2024-08-26T10:48:00";

countdownTimer(endDate);
