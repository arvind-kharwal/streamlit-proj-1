import streamlit as st

about_page = st.Page(
    page = 'views/about.py',
    title= 'About us',
    icon=':material/account_circle:',
    default=True
)
service_page =st.Page(
    page='views/service.py',
    title='Our Services',
    icon=':material/person:',
)

contact_page = st.Page(
    page='views/contact.py',
    title='Contact us',
    icon = ':material/supervisor_account:'
)

dpage=st.Page(
    page='views/department.py',
    title='Departments',
    icon = ':material/supervisor_account:'
)

ppage=st.Page(
    page='views/project.py',
    title='Projects',
    icon = ':material/supervisor_account:'
)

# nm = st.navigation(pages=[about_page,service_page,contact_page,dpage,ppage])

nm = st.navigation(
    {
        "Info": [about_page,service_page,contact_page ],
        "Useful Links": [dpage,ppage],
    }
)
st.logo('assets/house.png')
nm.run()
