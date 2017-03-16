  $(document).ready(function(){
    $('.slider').slider({
        full_width: true,
        indicators: false,
        interval: 2000

      });
    $('.parallax').parallax();
    $('.tooltipped').tooltip({delay: 50});
    $('.datepicker').pickadate({
        selectMonths: true, // Creates a dropdown to control month
        selectYears: 15, // Creates a dropdown of 15 years to control year
        format: 'yyyy-mm-dd'
     });
    $(".button-collapse").sideNav(); 
    $('.info_text').readmore({
          collapsedHeight: 163,
    });
    $('.gallery').readmore({
          collapsedHeight: 740,
          moreLink: '<a href="#">View more</a>',
          lessLink: '<a href="#">Close</a>'
    });
    $('.coffee_blog_text').readmore({
          collapsedHeight: 200,
    });

    $('.article').readmore({
        collapsedHeight: 194
    });
    $('.text_length').readmore({
        collapsedHeight: 180
    });
});

