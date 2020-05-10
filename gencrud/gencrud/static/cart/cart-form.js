/*
 * import: cart/cart-components.js
 * import: error/error-components.js
 * 
*/

class CartForm extends BaseModalForm {
    constructor(component, componentFn, productId) {
        super(component);

        this.componentFN = CartComponent;
        this.productId = productId;
        this.dataTarget = this.componentFN.dataTarget;

        this.setForm.bind(this);
        this.remove.bind(this);
    }

    static postSuccess(that, data, dataProductCart) {
        dataProductCart['totalPrice'] = data['totalPrice'];
        
        document.body.insertAdjacentHTML('afterend',
            that.componentFN(dataProductCart).html
        );

        const wrapperNode = document.getElementById(that.dataTarget);
        const targetDelPopup = wrapperNode.querySelector('.del_popup');

        targetDelPopup.addEventListener('click', that.remove.bind(that));
        document.addEventListener('click', that.remove.bind(that)); 

        const topNavbar = document.getElementById('top');
        console.log('current data order:', data);
        console.log(topNavbar);
        console.log(CartTopIcon().html);
    }


    static postError(that, errors) {
        console.log(Object.values(errors));
        
        document.body.insertAdjacentHTML('afterend',
            ErrorsComponent(Object.values(errors)).html
        );

        const wrapperNode = document.getElementById(that.dataTarget);
        const targetDelPopup = wrapperNode.querySelector('.del_popup');

        targetDelPopup.addEventListener('click', that.remove.bind(that));
        document.addEventListener('click', that.remove.bind(that));
        // alert(`
        // Мы знаем и работаем над этой проблемой!
        // Попробуйте сделать заявку на этот товар.
        // Или, сообщите нам любым удобным для вас способом.
        // Тикет #58`);
    }

    setForm(event) {
        if (this.wrapperNode) { 
            throw new Error(`ID:"${this.dataTarget}" form exists already!`); 
        }

        this.productId = event.target.dataset.productPk;

        let that = this;

        fetchGetProduct(this.productId, that).then(data => {
            let dataProductCart = {
                id:     data.pk,
                title:  data.title,
                units:  data.units || that.componentFN.units,
                productItems:   that.mapProductItemsList(data.product_items),
                totalPrice:     0 // that.getTotalPrice(data.productItemsList),
            }


            $.post(that.component.action, dataProductCart).done(function (response) {
                if (response.success) {
                    CartForm.postSuccess(that, response.success, dataProductCart);
                } else {
                    CartForm.postError(that, response.errors);
                }
            });
        });
    }

    remove(event) {
        const wrapperNode = event.target && event.target.closest(`#${this.dataTarget}`) 
            || document.getElementById(`${this.dataTarget}`);

        wrapperNode && wrapperNode.remove();
    }

    mapProductItemsList(product_items) {
        const checkedOnPage = this._checkedCheckboxesOnPage();

        let productItemsList = [];
        [...checkedOnPage].forEach(function(node) {
                const inputCount = document.getElementById(`product_item_count_${node.value}`);
                
                const pk = node.value;
                const itemProduct = product_items.filter((e) => (+e.pk === +pk))[0];
                const totalPrice = +itemProduct.price * +inputCount.value;

                const productItem = {
                    id: pk,
                    title: itemProduct.name,  // node.closest('div').querySelector('label').innerText,
                    count: inputCount.value,
                    price: Boolean(itemProduct.price) ? itemProduct.price : 0,
                    totalPrice: totalPrice
                };

                productItemsList.push(productItem);
            });

        return productItemsList;
    }

    _checkedCheckboxesOnPage() {
        const named = CustomCheckboxGroupComponent().named;
        const productItemQS = `input[name="${named}"]`;
        return document.querySelectorAll(`${productItemQS}:checked`);
    }
}

async function fetchGetProduct(productId, that) {
    const url = `/api/products/${productId}/`;
    return await fetch(url).then(response => response.json())
}

