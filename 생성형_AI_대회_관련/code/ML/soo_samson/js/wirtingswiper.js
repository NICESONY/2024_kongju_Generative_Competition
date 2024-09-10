    
  var mySwiper = new Swiper ('.swiper-container', {
    speed: 400,
    spaceBetween: 30,
    initialSlide: 0,
    //truewrapper adoptsheight of active slide
    autoHeight: false,
    // Optional parameters
    direction: 'horizontal',
    loop: true,
    // delay between transitions in ms
    autoplay: 5000,
    autoplayStopOnLast: false, // loop false also
    // If we need pagination
    pagination: '.swiper-pagination',
    paginationType: "bullets",
    
    // Navigation arrows
    nextButton: '.swiper-button-next',
    prevButton: '.swiper-button-prev',
    
    // And if we need scrollbar
    //scrollbar: '.swiper-scrollbar',
    // "slide", "fade", "cube", "coverflow" or "flip"
    effect: 'slide',
    // Distance between slides in px.
    spaceBetween: 30,
    //
    slidesPerView: 3,
    //
    centeredSlides: true,
    //
    slidesOffsetBefore: 0,
    //
    grabCursor: true,
  })        
 