<template>

  <div class="attempt-box" :class="{selected: selected}">
    <template v-if="isAnswer">
      <mat-svg
        v-if="interaction.correct"
        class="svg-item svg-correct"
        category="action"
        name="check_circle"
      />
      <mat-svg
        v-if="!interaction.correct"
        class="svg-item svg-wrong"
        category="navigation"
        name="cancel"
      />
    </template>
    <mat-svg
      v-else-if="isHint"
      class="svg-item svg-hint"
      category="action"
      name="lightbulb_outline"
    />
  </div>

</template>


<script>

  module.exports = {
    props: {
      interaction: {
        type: Object,
        required: true,
      },
      selected: {
        type: Boolean,
        required: true,
      },
    },
    computed: {
      isAnswer() {
        return this.interaction.type === 'answer';
      },
      isHint() {
        return this.interaction.type === 'hint';
      },
    },
  };

</script>


<style lang="stylus" scoped>

  @require '~kolibri.styles.definitions'

  .attempt-box
    background-color: $core-bg-light
    border-radius: 10px
    height: 60px
    width: 60px
    padding: 10px
    float: left
    margin-right: 10px
    cursor: pointer
    display: inline-block
    border: 2px solid $core-text-disabled

  .selected
    border: 2px solid $core-text-default

  .svg-item
    height: 38px
    width: auto
    border-bottom: 2px solid $core-text-default
    padding: 2px

  .svg-hint
    fill: $core-text-annotation

  .svg-wrong
    fill: $core-status-wrong

  .svg-correct
    fill: $core-status-correct

</style>
