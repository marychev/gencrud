const sleep = (milliseconds) => new Promise(resolve => setTimeout(resolve, milliseconds));


class AbstractModalForm {
	_showValidInput() { throw new Error('Not inplementation!'); }

	init() { throw new Error('Not inplementation!'); }
	open() { throw new Error('Not inplementation!'); }
	setForm() { throw new Error('Not inplementation!'); }
	remove() { throw new Error('Not inplementation!'); }
	clean() { throw new Error('Not inplementation!'); }

	listenerEvents() { throw new Error('Not inplementation!'); }
	isValid() { throw new Error('Not inplementation!');	}
	
	inputEmail() { throw new Error('Not inplementation!'); }
	isValidEmail() { throw new Error('Not inplementation!'); }
	onBlurEmail() { throw new Error('Not inplementation!'); }

	inputPhone() { throw new Error('Not inplementation!'); }
	isValidPhone() { throw new Error('Not inplementation!'); }
	onBlurPhone() { throw new Error('Not inplementation!'); }

	inputComment() { throw new Error('Not inplementation!'); }
	isValidComment() { throw new Error('Not inplementation!'); }
	onBlurComment() { throw new Error('Not inplementation!'); }

	buttonSubmit() { throw new Error('Not inplementation!'); }
	buttonSubmitDisabled() { throw new Error('Not inplementation!'); }
	onClickSubmit() { throw new Error('Not inplementation!'); }
}


class BaseModalForm extends AbstractModalForm {
	constructor(component) {
		super(component);

		this._isSent = false;
		this.component = component;
		this.dataTarget = component.dataTarget;
	}

	get wrapperNode() { return document.getElementById(this.dataTarget); }
	get form() { return this.wrapperNode && this.wrapperNode.getElementsByTagName('form')[0]; }
	
	get formData() { return $(this.form).serializeArray(); }
	
	get title() { return this.wrapperNode && this.wrapperNode.querySelector('.modal-title'); }
	set title(title) { this.title.innerText = title; }

	get isSent() { return this._isSent; }
	set isSent(isSent) {
		this._isSent = isSent;
		
		if (isSent) {
			this._isSent = true;
			this.buttonSubmitDisabled.bind(this, true);
		}
	}

	init() {
		const that = this;
		const targets = document.querySelectorAll([`[data-target="#${that.dataTarget}"]`]);

		[...targets].forEach(function(node) {
			node.addEventListener('click', that.open.bind(that));
		});
	}
	
	open(event) { !this.wrapperNode ? this.setForm(event) : null; }
	setForm(event) {
		if (this.wrapperNode) { 
			throw new Error(`ID:"${this.dataTarget}" form exists already!`); 
		}
		
		document.body.insertAdjacentHTML('afterend', this.component.html);

		this.wrapperNode.addEventListener('click', this.listenerEvents.bind(this));
		this.wrapperNode.addEventListener('blur', this.listenerEvents.bind(this));
	}
		
	remove() {
		$(`#${this.dataTarget}`).modal('hide');  
		this.wrapperNode && this.wrapperNode.remove();

		this.isSent = false;
	}
}
