<span class="mention-me " data-kwai-user-id="580564424462">@徐东亿</span>  <template>
  <div>
    <div class="button-group">
      <button class="left-button">按钮1</button>
      <div class="right-buttons">
        <button>按钮2</button>
        <button>按钮3</button>
      </div>
    </div>
    <p class="description">这是一段文字描述</p>
  </div>
</template>

<style>
  .button-group {
    display: flex;
    justify-content: space-between;
    margin-bottom: 20px;
  }

  .left-button {
    order: 1;
  }

  .right-buttons {
    display: flex;
    justify-content: flex-end;
    order: 2;
  }

  button {
    padding: 8px 16px;
    background-color: #f0f0f0;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    margin-left: 10px;
  }

  .description {
    font-size: 16px;
    line-height: 1.5;
  }
</style>
 耗时：2857 ms