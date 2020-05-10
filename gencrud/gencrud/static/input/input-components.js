const InputUserHiddenComponent = (userId) => {
    const that = InputUserHiddenComponent;
    that.id = 'id_user';
    that.named = 'user';
    that.type = 'hidden';


    return {
        html: `<input type="${that.type}" name="${that.named}" value="${userId}" id="${that.id}">`
    }
};


const InputEmailGroupComponent = (email) => { 
    const that = InputEmailGroupComponent;
    that.id = 'id_email';
    that.named = 'email';
    that.type = 'email';
    that.required = 'required';

    return {
        named: that.named,
        value: email,
        html: `<div class="form-group">
            <input type="${that.type}" name="${that.named}" value="${email}" ${that.required} id="${that.id}" 
                class="form-control" placeholder="your@email.com">
        </div>`
    }
};


const InputPhoneGroupComponent = (phone) => { 
    const that = InputPhoneGroupComponent;
    const helpText = `Мы никогда не передадим вашу электронную почту кому-либо еще.`;
    const helpNode = `<div class="form-text text-muted small">${helpText}</div>`;

    that.id = 'id_phone';
    that.named = 'phone';
    that.type = 'text';
    that.required = '';

    return {

        value: phone,
        html: `<div class="form-group">
            <input type="${that.type}" name="${that.named}" value="${phone}" ${that.required} id="${that.id}" 
                class="form-control" placeholder="Телефон">
            ${helpNode}
        </div>`
    }
};


const TextareaCommentGroupComponent = () => { 
    const that = TextareaCommentGroupComponent;
    const cols = 40;
    const rows = 4;

    that.id = 'id_comment';
    that.named = 'comment';
    that.type = 'textarea';
    that.required = 'required';

    return {
        type: that.type,
        html: `<div class="form-group">
            <textarea id="${that.id}" name="${that.named}" cols="${cols}" rows="${rows}" 
                placeholder="Ваш коментарий" class="form-control"></textarea>
        </div>`
    }
};


const SubmitButtonComponent = (disabled = true) => {
    const that = SubmitButtonComponent;
    const versionText = ['Отправить', 'Отправлено', 'Не все поля заполнены'];

    that.type = 'submit';
    that.className = 'btn btn-block btn-primary';
    that.text = versionText[0];

    return {
        text: that.text,
        html: disabled 
            ? `<p><button disabled type="${that.type}" class="${that.className}">${that.text}</button></p>`
            : `<p><button type="${that.type}" class="${that.className}">${that.text}</button></p>`
    }
};
