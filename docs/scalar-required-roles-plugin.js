class RequiredRolesBlock extends HTMLElement {
  connectedCallback() {
    let roles = []
    try {
      roles = JSON.parse(this.getAttribute('data-value') || '[]')
    } catch (e) {
      roles = []
    }
    if (!Array.isArray(roles) || roles.length === 0) {
      this.innerHTML = ''
      return
    }

    const items = roles
      .map((role) => `<li class="font-code text-c-2">${role}</li>`)
      .join('')

    this.innerHTML = `
      <div class="mt-6">
        <div class="text-c-1 mt-3 mb-3 text-lg leading-[1.45] font-medium">
          Required Roles
        </div>
        <ul class="mb-3 list-none p-0 text-sm">
          ${items}
        </ul>
      </div>
    `
  }
}

if (!customElements.get('required-roles-block')) {
  customElements.define('required-roles-block', RequiredRolesBlock)
}

export default () => ({
  name: 'required-roles-plugin',
  extensions: [
    {
      name: 'x-roles-required',
      component: (value) => {
        const el = document.createElement('required-roles-block')
        el.setAttribute('data-value', JSON.stringify(value))
        return el
      },
    },
  ],
})