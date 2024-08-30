// Horizontal Swiper
const swiperHorizontal = new Swiper('.swiper-horizontal', {
  // Optional parameters
  direction: 'horizontal',
  loop: true,

  // If we need pagination with dynamic bullets
  pagination: {
      el: '.swiper-pagination-horizontal',
      dynamicBullets: true,
  },
});

// Vertical Swiper (Corrected Direction)
const swiperVertical = new Swiper('.swiper-vertical', {
  // Optional parameters
  direction: 'vertical',  // Corrected to vertical
  loop: true,

  // Pagination
  pagination: {
      el: '.swiper-pagination-vertical',
  },

  // Navigation arrows
  navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
  },

  // Scrollbar
  scrollbar: {
      el: '.swiper-scrollbar',
  },
});

// General Swiper (e.g., for a basic image slider)
const swiperGeneral = new Swiper('.mySwiper', {
  slidesPerView: 1,
  spaceBetween: 30,
  loop: true,
  pagination: {
      el: ".swiper-pagination",
      clickable: true,
  },
  navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
  },
});



document.addEventListener('DOMContentLoaded', function () {
  var swiper = new Swiper('.mySwiper', {
      slidesPerView: 1,
      spaceBetween: 10,
      pagination: {
          el: '.swiper-pagination',
          clickable: true,
      },
  });

  var swiper2 = new Swiper('.mySwiper2', {
      slidesPerView: 1,
      spaceBetween: 10,
      pagination: {
          el: '.swiper-pagination',
          clickable: true,
      },
  });
});


document.querySelectorAll('.tab-container input[type="radio"]').forEach(input => {
    input.addEventListener('change', function() {
        document.querySelectorAll('.tab-content').forEach(content => {
            content.style.display = 'none'; // 모든 탭 내용을 숨깁니다.
        });
        document.getElementById('content-' + this.id).style.display = 'block'; // 선택된 탭의 내용을 표시합니다.
    });
});

function showContent(id) {
    var contents = document.querySelectorAll('.tab-content');
    contents.forEach(function(content) {
        content.classList.remove('active');
    });

    var activeContent = document.getElementById(id);
    if (activeContent) {
        activeContent.classList.add('active');
    }
}



const swiper = new Swiper('.swiper', {
    // Optional parameters
    direction: 'horizontal',
    loop: true,
    
    pagination: {
        el: '.swiper-pagination',
      },

      
});
 





