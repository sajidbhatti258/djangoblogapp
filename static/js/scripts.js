// const swiper = new Swiper('.swiper', {
//     direction: 'horizontal', // Slider moves horizontally
//     loop: true,              // Enables looping
//     autoplay: {              // Autoplay configuration
//         delay: 3000,
//         disableOnInteraction: false,
//     },
//     navigation: {            // Next and Previous buttons
//         nextEl: '.swiper-button-next',
//         prevEl: '.swiper-button-prev',
//     },
//     slidesPerView: 1,        // Show only one slide at a time
//     spaceBetween: 10,        // Space between slides
//     breakpoints: {           // Add responsiveness if needed
//         640: { slidesPerView: 1 }, // For smaller screens
//         768: { slidesPerView: 1 }, // For tablets
//         1024: { slidesPerView: 1 }, // For desktops
//     },
// });
tinymce.init({
    selector: 'textarea',
    forced_root_block: '',
    clean_paste: true,
});

var swiper = new Swiper('.swiper', {
    slidesPerView: 1, // Initial view on small screens
    centeredSlides: true, // Center the first slide
    loop: true, // Infinite scrolling
    spaceBetween: 10, // Space between slides

    // Breakpoints for larger screens (Desktop)
    breakpoints: {
        768: {
            slidesPerView: 3, // Show 3 slides on desktop
            spaceBetween: 30, // Space between slides on desktop
        },
        1024: {
            slidesPerView: 3, // Ensure 3 slides on larger desktop screens as well
            spaceBetween: 40, // More space between slides for larger screens
        },
    },

    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
});



