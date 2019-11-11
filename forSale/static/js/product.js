$(function() {
    //모바일 분기 처리 - 모바일 작업 되기 전까지만 유지
    var filter = "win16|win32|win64|mac|macintel";
    if (navigator.platform) {
        if (filter.indexOf(navigator.platform.toLowerCase()) < 0) {
            $(".contents").removeClass('contents');
            $('.main1_bg, .main1_bg2, .main1_con, .main1_visual, .intro_txt, .intro_cloud, .intro_wrap, .intro_menu, .intro_fix, .intro_ani, .exem .intro video, .wheel').css('position', 'absolute');
            $(".wheel").css('display', 'none');
            $(".section").css('min-height', '900px');
            $(".last_div").css('min-height', '0');
            $('.info_value').addClass('ani');
            $('.summary_ul li .icon, .summary_ul li .txt').addClass('ani');
            $('.intro').css({
                width: '1500px',
                overflow: 'hidden'
            });
        } else {

        }
    }

    //헤더, SNS 색상
    $('.sns, .lang').addClass('white');
    $('header').addClass('htran');

    //섹션별 이벤트
    $('.contents').fullpage({
        licenseKey: 'E42D1232-7E6743B8-ADEF5F26-A4E052DE',
        menu: '.sub_menu',
        anchors: ['intro', 'con1', 'con2', 'con3', 'con4', 'con5', 'bottom'],
        verticalCentered: true,
        css3: true,
        navigation: false,
        scrollBar: true,
        hybrid: true,
        fitToSection: false,
        afterLoad: function(anchorLink, index) {

            $.fn.fullpage.setKeyboardScrolling(index == 1 || index == 2);
            if (index.anchor == 'intro') {
                $('.sns, .wheel, .lang').removeClass('ani');
                $('.main1_bg').css('position', 'fixed');
                $('.intro_fix, .intro_ani').css('display', 'block');
                $('header').addClass('htran');
                $('.btn_layer').addClass('ani').css('bottom', '-300px');
            }
            if (index.anchor == 'con1') {
                $('.sns, .wheel, .lang').removeClass('ani');
                $('.main1_bg').css('position', 'fixed');
                $('.btn_layer').removeClass('ani').css('bottom', '30px');
            }
            if (index.anchor == 'con2') {
                $('.sns, .wheel, .lang').removeClass('ani');
                $('.main1_bg').css('position', 'fixed');
            }
            if (index.anchor != 'intro') {
                $('.sns, .wheel, .lang').addClass('ani');
                $('.summary_ul li:nth-child(1) .icon, .summary_ul li:nth-child(1) .txt').addClass('ani');
                setTimeout(function() {
                    $('.summary_ul li:nth-child(2) .icon, .summary_ul li:nth-child(2) .txt').addClass('ani');
                }, 100);
                setTimeout(function() {
                    $('.summary_ul li:nth-child(3) .icon, .summary_ul li:nth-child(3) .txt').addClass('ani');
                }, 300);
                setTimeout(function() {
                    $('.summary_ul li:nth-child(4) .icon, .summary_ul li:nth-child(4) .txt').addClass('ani');
                }, 600);
            }
            if (index.anchor == 'con4') {
                $('.btn_layer').css('bottom', '30px');
            }
            if (index.anchor == 'con5') {
                $('.btn_layer').css('bottom', '162px');
            }

        },
        onLeave: function(index, newIndex, direction) {
            if (index == 2 && direction == "up") {
                $('.sns, header .lang').addClass('ani');
            }
        }
    });
    //스크롤 이벤트
    $(window).scroll(function() {
        var st = $(window).scrollTop();

        if ($('.summary').offset().top - 100 <= st) {
            $('header').addClass('htran');
        }
        if ($('.summary').offset().top <= st) {
            $('header').removeClass('htran');
        }


        if ($('.summary').offset().top + 10 <= st) {
            $('.intro_fix, .intro_ani').css('display', 'block');
        }

        if ($('.summary').offset().top + 500 <= st) {
            $('.intro_fix, .intro_ani').css('display', 'none');
        }

        //제품개요 영상 종료
        if ($('.feature').offset().top <= st) {
            $('.summary_video .video').html('');
            $('.summary_video .btn_play').show();
        }

    });

    //제품 DEMO
    $('.btn_demo, .last_div .btn_border').click(function() {
        $('.pop').fadeIn(400);
        $('body').css({
            height: '100%',
            overflow: 'hidden',
            overflowY: 'hidden'
        });
    });
    $('.pop .btn_close, .pop_bg').click(function() {
        $('.pop').fadeOut(400);
        $('body').css({
            height: 'auto',
            overflowY: 'scroll'
        });
    });



});



//제품 스팩 탭
function tech_ul(num) {
    var tf = $('.tech_ul').find('li');
    for (var i = 0; i < tf.length; i++) {
        if (i == num) {
            tf.eq(i).addClass('on');
            $('.tech_con' + i).slideDown(0);
        } else {
            tf.eq(i).removeClass('on');
            $('.tech_con' + i).slideUp(0);
        }
    }
}