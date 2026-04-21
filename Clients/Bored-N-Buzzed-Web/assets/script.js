document.addEventListener('DOMContentLoaded', () => {
    // 1(Mon) to 7(Sun), but JS getDay() is 0(Sun) to 6(Sat).
    // Let's map JS days to our data-day attributes:
    // JS 1(Mon) -> data-day 1
    // JS 2(Tue) -> data-day 2
    // JS 3(Wed) -> data-day 3
    // JS 4(Thu) -> data-day 4
    // JS 5(Fri) -> data-day 5
    // JS 6(Sat) & 0(Sun) -> highlight Bulk Up Weekend card

    const todayJS = new Date().getDay();
    let targetDay = todayJS;

    const dealCards = document.querySelectorAll('.deal-card');

    if (todayJS >= 1 && todayJS <= 5) {
        // Weekday
        dealCards.forEach(card => {
            if(card.getAttribute('data-day') == targetDay) {
                card.classList.add('active-day');
                // Change the active pill text to TODAY'S DROP
                const pill = card.querySelector('.pill-badge');
                if(pill && !pill.classList.contains('yellow-badge')) {
                    pill.textContent = "TODAY'S DROP";
                    pill.classList.add('yellow-badge');
                }
            }
        });
    } else {
        // Weekend (Saturday=6, Sunday=0)
        // Highlight the Bulk Up Weekend card
        const weekendCard = document.querySelector('.highlight-card');
        if(weekendCard) {
            weekendCard.classList.add('active-day');
            const pill = weekendCard.querySelector('.pill-badge');
            if(pill) pill.textContent = "LIVE NOW";
        }
    }
});
