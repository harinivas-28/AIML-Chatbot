css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex; border-color: #ff751a
}
.chat-message.user {
    background-color: #809fff
}
.chat-message.bot {
    background-color: #809fff
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #000;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://yt3.ggpht.com/a/AATXAJxfvfJ5llxBhMWICqAPVHg-0bQ4ASNaqbCn1Q=s900-c-k-c0xffffffff-no-rj-mo" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://cdn3.iconfinder.com/data/icons/avatars-flat/33/man_5-1024.png">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''