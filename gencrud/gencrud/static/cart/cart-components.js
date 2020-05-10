/* 
 * import: error/error-components.js
*/


const CartLinkComponent = () => {
    const that = CartLinkComponent;
    that.url = '/cart/';

    return { 
        html: `<a class="text-left" href="${that.url}"><b class="fa fa-shopping-cart"></b></a>`
    }
};


const CartProductListComponent = (data, units) => {
    const that = CartProductListComponent;
    const productList = data && data.map((e) => (
        `<li class="small">${e.title} - <b>${e.count} </b><small class="text-muted"> ${units}</small></li>`
    ));

    return {
        html: `<ul>${productList && productList.join('')}</ul>`
    }
};


const CartProductComponent = (data) => {
    const that = CartProductComponent; 
    const rub = '&#8381;' // '&#x20bd;'

    that.units = data && data.units || 'шт.';
    that.title = data && data.title || 'Корзина пуста';
    that.totalPrice = data && data.totalPrice || 0;
    that.productItems = data && data.productItems;

    return {
        units: that.units,
        html: `<li><span>${that.title}</span> - <b>${that.totalPrice} </b><small class="text-muted">${rub}</small>
            <ul>
                ${CartProductListComponent(that.productItems, that.units).html}
            </ul>
        </li>`
    }
};


const CartComponent = (data = null) => {
    const that = CartComponent;
    const title = `<b>ТОВАР ДОБАВЛЕН!</b> ${CartLinkComponent().html}<br>`;
	
    that.dataTarget = 'cart-form';
	that.action = '/cart/add/';

	return {
		dataTarget: that.dataTarget,
		action: that.action,
        html: `<div id="${that.dataTarget}" class="msg_add_cart">
            <ol>${title}
            ${CartProductComponent(data).html} 
            </ol>
            <a class="del_popup">x</a>
        </div>`
    }
};


const CartTopIcon = (data) => {
    console.log(data, '<<<');

    const link = `<a href="${CartLinkComponent.url}" class="btn btn-sm btn-outline-secondary">`

    const htmlHasProduct = data && data.length > 0 && `<span class="small">
        <span>${data.length}</span>/<span>${data.totalCountProductItems}</span></span>
        <span class="small text-muted">
            <small>{{ cart.0.totalPrice }}</small>
        </span>`;

    return {
        html: `<a href="/cart/" class="btn btn-sm btn-outline-secondary">
            <b class="fa fa-shopping-cart"></b>
            ${htmlHasProduct}
        </a>`
    }
}