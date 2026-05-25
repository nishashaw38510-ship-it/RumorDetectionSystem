const ctx = document.getElementById('myChart');

new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['Mon','Tue','Wed','Thu','Fri','Sat'],
        datasets: [{
            label: 'Rumor Detection',
            data: [12,19,8,15,22,30],
            borderWidth: 3
        }]
    },
    options: {
        responsive:true
    }
});