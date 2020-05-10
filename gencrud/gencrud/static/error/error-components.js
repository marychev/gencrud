const ErrorsComponent = (errors) => {
    const that = ErrorsComponent; 
    that.dataTarget = 'cart-form';

    const errorsList = errors && errors.map((e) => (
        `<li class="small">${e}</li>`
    ));

    return {
        dataTarget: that.dataTarget,
        html: `<div id="${that.dataTarget}" class="msg_add_cart bg-danger">
        <b>Обнаружены ошибки:</b>
        <ol>${errorsList && errorsList.join('')}</ol>
        <a class="del_popup">x</a>
        </div>`
    }
};