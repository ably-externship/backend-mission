$(document).ready(function() {
    $('.action-button-box button').click(function() {
        const $basket = $(this).parent();
        const id = $basket.data('id');
        const ajaxSetting = {
            dataType: 'json',
        };
        if ($(this).hasClass('edit-button')) {
            const qty = $basket.siblings('p').find('input[name=qty]').val();
            const param = {
                "count": qty,
            };
            ajaxSetting.url = `/basket/${id}/update/`;
            ajaxSetting.data = JSON.stringify(param);
            ajaxSetting.type = 'post';
        } else if ($(this).hasClass('remove-button')) {
            ajaxSetting.url = `/basket/${id}/delete/`;
            ajaxSetting.type = 'get';
        }
        $.ajax({
            ...ajaxSetting,
            success: function(res) {
                if (res.result && res.action == 'delete') {
                    alert('장바구니에서 품목에 삭제되었습니다.');
                    $basket.closest('li.item').remove();
                } else if (res.result && res.action == 'update') {
                    alert('장바구니에서 품목이 수정되었습니다.');
                }
            }
        });
    });
});