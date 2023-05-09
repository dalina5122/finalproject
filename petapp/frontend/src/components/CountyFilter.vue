<template>
    <div>
        Click on a county to filter the list:
    </div>
    <div class="county-rows">
        <!-- FIRST ROW -->
        <div class="county-row">
            <div
            v-for="(county, index) in counties.slice(0, 4)"
            :key="index"
            class="county-item"
            @click="selectCounty(county.code)"
            >
            <img :src="county.image" :alt="county.name" loading="auto" class="county-image" />
            </div>
        </div>

        <!-- SECOND ROW -->
        <div class="county-row">
            <div
                v-for="(county, index) in counties.slice(4, 5)"
                :key="index"
                class="county-item tall-county"
                @click="selectCounty(county.code)"
            >
                <img :src="county.image" :alt="county.name" loading="auto" class="county-image" />
            </div>

            <div class="county-column">
                <div class="county-row">
                <div
                    v-for="(county, index) in counties.slice(5, 7)"
                    :key="index"
                    class="county-item"
                    @click="selectCounty(county.code)"
                >
                    <img :src="county.image" :alt="county.name" loading="auto" class="county-image" />
                </div>
                </div>
                <div class="county-row">
                <div
                    v-for="(county, index) in counties.slice(7, 9)"
                    :key="index"
                    class="county-item"
                    @click="selectCounty(county.code)"
                >
                    <img :src="county.image" :alt="county.name" loading="auto" class="county-image" />
                </div>
                </div>
            </div>

            <div
                v-for="(county, index) in counties.slice(9, 10)"
                :key="index"
                class="county-item tall-county"
                @click="selectCounty(county.code)"
            >
                <img :src="county.image" :alt="county.name" loading="auto" class="county-image" />
            </div>

            <div class="county-column">
                <div class="county-row">
                <div
                    v-for="(county, index) in counties.slice(10, 12)"
                    :key="index"
                    class="county-item"
                    @click="selectCounty(county.code)"
                >
                    <img :src="county.image" :alt="county.name" loading="auto" class="county-image" />
                </div>
                </div>
                <div class="county-row">
                <div
                    v-for="(county, index) in counties.slice(12, 14)"
                    :key="index"
                    class="county-item"
                    @click="selectCounty(county.code)"
                >
                    <img :src="county.image" :alt="county.name" loading="auto" class="county-image" />
                </div>
                </div>
            </div>
        </div>

        <!-- THIRD ROW -->
        <div class="county-row">
            <div class="county-column">
                <div class="county-row">
                <div
                    v-for="(county, index) in counties.slice(14, 16)"
                    :key="index"
                    class="county-item third-row"
                    @click="selectCounty(county.code)"
                >
                    <img :src="county.image" :alt="county.name" loading="auto" class="county-image" />
                </div>
                </div>
                <div class="county-row">
                <div
                    v-for="(county, index) in counties.slice(16, 18)"
                    :key="index"
                    class="county-item third-row"
                    @click="selectCounty(county.code)"
                >
                    <img :src="county.image" :alt="county.name" loading="auto" class="county-image" />
                </div>
                </div>
            </div>

            <div
                v-for="(county, index) in counties.slice(18, 23)"
                :key="index"
                class="county-item tall-county third-row"
                @click="selectCounty(county.code)"
            >
                <img :src="county.image" :alt="county.name" loading="auto" class="county-image" />
            </div>
        </div>

        <!-- FOURTH ROW -->
        <div class="county-row">
            <div
                v-for="(county, index) in counties.slice(23, 32)"
                :key="index"
                class="county-item fourth-row"
                @click="selectCounty(county.code)"
            >
                <img :src="county.image" :alt="county.name" loading="auto" class="county-image" />
            </div>
        </div>

        <!-- FIFTH ROW -->
        <div class="county-row">
            <div
                v-for="(county, index) in counties.slice(32, 36)"
                :key="index"
                class="county-item tall-county"
                @click="selectCounty(county.code)"
            >
                <img :src="county.image" :alt="county.name" loading="auto" class="county-image" />
            </div>

            <div class="county-column">
                <div class="county-row">
                <div
                    v-for="(county, index) in counties.slice(36, 38)"
                    :key="index"
                    class="county-item"
                    @click="selectCounty(county.code)"
                >
                    <img :src="county.image" :alt="county.name" loading="auto" class="county-image" />
                </div>
                </div>
                <div class="county-row">
                <div
                    v-for="(county, index) in counties.slice(38, 40)"
                    :key="index"
                    class="county-item"
                    @click="selectCounty(county.code)"
                >
                    <img :src="county.image" :alt="county.name" loading="auto" class="county-image" />
                </div>
                </div>
            </div>

            <div
                v-for="(county, index) in counties.slice(40, 41)"
                :key="index"
                class="county-item tall-county"
                @click="selectCounty(county.code)"
            >
                <img :src="county.image" :alt="county.name" loading="auto" class="county-image" />
            </div>

        </div>
    </div>
  </template>
  

<script>
export default {
  props: ["counties"],
  methods: {
    selectCounty(code) {
      this.$emit("county-selected", code);
    },
  },
};
</script>

<style scoped>
.county-rows {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.county-row {
  display: inline-flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.county-column {
  display: flex;
  flex-direction: column;
  flex-grow: 1;
  margin-left: 1rem;
}

.county-item {
  cursor: pointer;
  margin-left: 5px;
  margin-right: 15px;
  margin-top: -10px;
  margin-bottom: -20px;
  width: 100px;
  height: 100px;
}

.tall-county{
    height: 130px;
}

.fourth-row{
    margin-right: 1px;
}

.third-row{
    margin-right: 50px;
}

.county-image {
  width: 150%;
  height: 150%;
  object-fit: cover;
}
</style>








