$(document).ready(function() {
    //전체메뉴
    $('header h2').click(function() {
        $(this).addClass('on');
        $('body').css({
            height: '100%',
            overflow: 'hidden',
            overflowY: 'hidden'
        }).stop().animate({
            marginLeft: '-320px'
        }, 300);
        $('.btn_demo, header .lang').removeClass('ov').stop().animate({
            marginRight: '320px'
        }, 300);
        $('.sns').removeClass('ov').stop().animate({
            marginLeft: '-320px'
        }, 300);
        $('.exem .intro p').stop().animate({
            marginLeft: '-760px'
        }, 300);
        $('.exem_menu').stop().animate({
            marginLeft: '-800px'
        }, 300);
        $('.footer_partner, .footer_copy').stop().animate({
            marginRight: '320px'
        }, 300);

        $('.menu').stop().animate({
            marginRight: '0'
        }, 300);
        $('.main1_bg, .main1_bg2, .main1_con, .main1_visual, .intro_txt, .intro_cloud, .intro_wrap, .intro_menu, .intro_fix, .intro_ani, .exem .intro video, .wheel, .main_cube, .col_wrap').css('position', 'absolute');

        $('.menu_bg').show();
        $('.intro, .main1, .main2, .main3, .main4, .vision').addClass('fp-normal-scroll');

    });
    $('.menu a, .menu_bg').click(function() {
        $('header h2').removeClass('on');
        $('body').css({
            height: 'auto',
            overflowY: 'scroll'
        }).stop().animate({
            marginLeft: '0'
        }, 300);
        $('.btn_demo, header .lang').stop().animate({
            marginRight: '0'
        }, 300);
        $('.sns').removeClass('ov').stop().animate({
            marginLeft: '0'
        }, 300);
        $('.exem .intro p').stop().animate({
            marginLeft: '-600px'
        }, 300);
        $('.exem_menu').stop().animate({
            marginLeft: '-640px'
        }, 300);
        $('.footer_partner, .footer_copy').stop().animate({
            marginRight: '0'
        }, 300);

        $('.menu').stop().animate({
            marginRight: '-320px'
        }, 300).queue(function() {
            $('.main1_bg, .main1_bg2, .main1_con, .main1_visual, .intro_txt, .intro_cloud, .intro_wrap, .intro_menu, .intro_fix, .intro_ani,  .exem .intro video, .wheel, .main_cube, .col_wrap').css('position', 'fixed');
            $('.btn_demo, header .lang, .sns').addClass('ov');
        });

        $('.menu_bg').hide();
        $('.intro, .main1, .main2, .main3, .main4, .vision').removeClass('fp-normal-scroll');
    });

    // 아용약관
    $('.clause_form').css('height', $(window).height() - 140);
    $(window).bind('resize', function() {
        $('.clause_form').css('height', $(window).height() - 140);
    });
    $('.clause_con').css('height', $(window).height() - 195);
    $(window).bind('resize', function() {
        $('.clause_con').css('height', $(window).height() - 195);
    });

    $('.footer_copy ul li, .pop_agree a').click(function() {
        if ($('.clause').is(':hidden')) {
            $('body').css({
                height: '100%',
                overflow: 'hidden',
                overflowY: 'hidden'
            });
            $('.clause').fadeIn(400);
        }
    });
    $('.footer_copy .first, .pop_agree .first').click(function() {
        $(clause_tab(0)).click();
    });
    $('.footer_copy .last, .pop_agree .last').click(function() {
        $(clause_tab(1)).click();
    });
    $('.pop_agree .first, .pop_agree .last').click(function() {
        $('.clause_bg').css('opacity', '.35');
    });
    $('.clause .btn_close_b, .clause_bg').click(function() {
        $('.clause').fadeOut(400);
        $('.clause_bg').css('opacity', '.6');
        $('body').css({
            height: 'auto',
            overflowY: 'scroll'
        });
    });

    //지난 연도보기
    $('.news_category button').click(function() {
        if ($('.news_ul').is(':hidden')) {
            $('.news_ul').slideDown()
        } else {
            $('.news_ul').slideUp()
        }
    });
});

// 이용약관 탭 메뉴
function clause_tab(num) {
    var tf = $('.clause_tab').find('li');
    for (var i = 0; i < tf.length; i++) {
        if (i == num) {
            tf.eq(i).addClass('on');
            $('.clause_con' + i).show();
        } else {
            tf.eq(i).removeClass('on');
            $('.clause_con' + i).hide();
        }
    }
}