import streamlit as st
import base64

# CONFIG
st.set_page_config(page_title="Perfil", layout="wide")

# FUNÇÃO base64
def get_base64_image(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()
# ==================================================
# SEÇÃO - SITES PARCEIROS
# ==================================================
st.markdown("""
    <hr style="margin-top:50px; margin-bottom:30px;">

    <h2 style='
        text-align:center;
        font-size:38px;
        color:#333;
        margin-bottom:40px;
    '>
        Sites Parceiros
    </h2>
""", unsafe_allow_html=True)

link1, link2, link3 = st.columns(3)

# ================= LINK 1 =================
with link1:

    st.markdown("""
        <div style="text-align:center;">
            <img src="data:image/png;base64,{}"
                 style="
                    width:250px;
                    height:180px;
                    object-fit:cover;
                    border-radius:12px;
                 ">
        </div>
    """.format(get_base64_image("image_ifood.png")),
    unsafe_allow_html=True)

    st.markdown("""
        <h3 style="text-align:center; margin-top:15px;">
            iFood
        </h3>

        <p style="
            text-align:justify;
            font-size:16px;
            line-height:1.6;
        ">
            O iFood é uma plataforma de delivery que conecta
            restaurantes, mercados e consumidores, permitindo
            pedidos online de forma rápida e prática.
        </p>

        <div style="text-align:center; margin-top:15px;">
            <a href="https://portal.ifood.com.br/login"
               target="_blank"
               style="
                    font-size:20px;
                    text-decoration:none;
                    font-weight:bold;
               ">
                Acessar iFood
            </a>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ================= LINK 2 =================
with link2:

    st.markdown("""
        <div style="text-align:center;">
            <img src="data:image/png;base64,{}"
                 style="
                    width:250px;
                    height:180px;
                    object-fit:cover;
                    border-radius:12px;
                 ">
        </div>
    """.format(get_base64_image("image_facebook.jpg")),
    unsafe_allow_html=True)

    st.markdown("""
        <h3 style="text-align:center; margin-top:15px;">
            Facebook
        </h3>

        <p style="
            text-align:justify;
            font-size:16px;
            line-height:1.6;
        ">
            O Facebook é uma rede social utilizada para compartilhar
            fotos, vídeos, notícias e interagir com pessoas do mundo todo.
        </p>

        <div style="text-align:center; margin-top:15px;">
            <a href="https://www.facebook.com/?locale=pt_BR"
               target="_blank"
               style="
                    font-size:20px;
                    text-decoration:none;
                    font-weight:bold;
               ">
                Acessar Facebook
            </a>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ================= LINK 3 =================
with link3:


    st.markdown("""
        <div style="text-align:center;">
            <img src="data:image/png;base64,{}"
                 style="
                    width:250px;
                    height:180px;
                    object-fit:cover;
                    border-radius:12px;
                 ">
        </div>
    """.format(get_base64_image("image_netflix.jpg")),
    unsafe_allow_html=True)

    st.markdown("""
        <h3 style="text-align:center; margin-top:15px;">
            Netflix
        </h3>

        <p style="
            text-align:justify;
            font-size:16px;
            line-height:1.6;
        ">
            A Netflix é uma plataforma de streaming que oferece
            filmes, séries, documentários e conteúdos exclusivos
            para entretenimento online.
        </p>

        <div style="text-align:center; margin-top:15px;">
            <a href="https://www.netflix.com/br/"
               target="_blank"
               style="
                    font-size:20px;
                    text-decoration:none;
                    font-weight:bold;
               ">
                Acessar Netflix
            </a>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# WHATSAPP
# =========================
st.markdown(f"""
    <div style="text-align: center; margin-top: 50px;">
        <a href="https://wa.me/5583987220076" target="_blank">
            <img src="data:image/png;base64,{zap_base64}" width="100">
        </a>
    </div>
""", unsafe_allow_html=True)
