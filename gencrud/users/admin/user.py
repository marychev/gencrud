from gen.users.admin.base_user import BaseUserAdmin


class UserAdmin(BaseUserAdmin):
    pass

# --------------------------------------------------------------------------------------------------------
# def formfield_for_dbfield(self, db_field, **kwargs):
#     field = super(UserAdmin, self).formfield_for_dbfield(db_field, **kwargs)
#     print(kwargs['request'])
#     if db_field.name == 'is_staff':
#         print('hhhhh')
#         field.widget.attrs['disabled'] =  True # 'someclass ' + field.widget.attrs.get('class', '')
#     return field
#
# def get_changelist_form(self, request, **kwargs):
#     print('!!!!!!!!!!!!!1')
#     ft = super(UserAdmin, self).get_changelist_form(request, **kwargs)
#     print(self)
#     return ft
# --------------------------------------------------------------------------------------------------------
